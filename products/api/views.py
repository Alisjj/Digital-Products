# from lib2to3.pgen2.tokenize import TokenError
import os
from re import template
from subprocess import check_output
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from products.models import Category, Course, Lesson, Product, Section, UploadFile
from django.contrib.auth import get_user_model
from rest_framework import mixins
import requests
from django.http import HttpResponse, JsonResponse
from products.mixins import CourseAccesMixin
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from subscription.models import Pricing
from .serializers import LessonDetailSerializer, CourseSerializer, ProductSerializer, PurchasedProductSerializer, SectionSerializer
from django.conf import settings
from rave_python import Rave

User = get_user_model()
rave = Rave(os.getenv('FLW_PUBLIC_KEY'), os.getenv('RAVE_SECRET_KEY'))


class ProductListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(active=True)

class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        return self.request.user.userlibrary.products.all()
    


class UserProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

class ProductDestroy(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

class PurchasedProductsView(generics.ListAPIView):
    serializer_class = PurchasedProductSerializer

    def get_queryset(self):
        return self.request.user.userlibrary.products.all()

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.data['product_type'] == "subscription":
            if request.user.subscription.pricing.name == "Free":
                return Response("Upgrade your pricing plan", status=status.HTTP_401_UNAUTHORIZED)
        self.perform_create(serializer.save(user=request.user))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class CourseView(CourseAccesMixin, generics.CreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseRetrieve(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseDetail(generics.ListAPIView):
    serializer_class = SectionSerializer

    def get_queryset(self):
        course = get_object_or_404(Course, id=self.kwargs["course_id"])
        return course.sections.all()

class SectionDetailView(generics.ListAPIView):
    serializer_class = LessonDetailSerializer

    def get_queryset(self):
        course = get_object_or_404(Course, id=self.kwargs["course_id"])
        section = get_object_or_404(Section, id=self.kwargs["section_id"], course=course)
        return section.lessons.all()

        
        
    
@csrf_exempt
def flw_webhook(request, *args, **kwargs):
    secret_hash = settings.FLW_SECRET_HASH
    signature = request.headers.get("VERIF-HASH")
    event = json.loads(request.body)
    if signature == None or signature != secret_hash:
        return HttpResponse(status=401)


    if event['event'] == "charge.completed" and event['data']['status'] == "successful":

        tr_id = int(event['data']['id'])
        url = "https://api.flutterwave.com/v3/transactions/{}/verify".format(tr_id)
        res = requests.get(url=url, headers={
            "Authorization": settings.RAVE_SECRET_KEY
            })
        resp = res.json()
        event_type = resp['data']['meta']['event_type']

        if event_type == "subscription.checkout":
            flw_customer_email = resp['data']['customer']['email']
            plan_id = resp['data']['plan']
            params = {
                "email": flw_customer_email,
                "plan": plan_id,
            }

            sub_url = "https://api.flutterwave.com/v3/subscriptions"

            sub = requests.get(url=sub_url, headers={
            "Authorization": settings.RAVE_SECRET_KEY
            }, params=params)

            subs = sub.json()
            plan_id = subs["data"][0]["plan"]

            try:
                user = User.objects.get(email=flw_customer_email)
                user.subscription.status = subs['data'][0]['status']
                user.subscription.flw_subscription_id = subs['data'][0]['id']
                pricing = Pricing.objects.get(plan_id=plan_id)
                user.subscription.pricing = pricing
                user.subscription.save()
            except User.DoesNotExist:
                return HttpResponse("User Does not exist", status=status.HTTP_400_BAD_REQUEST)


        elif event_type == "product.checkout":
            product_id = resp['data']['meta']['product_id']
            flw_customer_email = resp['data']['customer']['email']
            try:
                user = User.objects.get(email=flw_customer_email)
                user.userlibrary.products.add(product_id)
                print("product added")
            except User.DoesNotExist:
                return HttpResponse("User Does not exist", status=status.HTTP_400_BAD_REQUEST)

        if event['event'] == "subscription.cancelled":
            flw_customer_email = event['data']['customer']['email']
            plan_id = event['plan']['id']
            params = {
                "email": flw_customer_email,
                "plan": plan_id,
            }

            sub_url = "https://api.flutterwave.com/v3/subscriptions"
            sub = requests.get(url=sub_url, headers={
            "Authorization": settings.RAVE_SECRET_KEY
            }, params=params)

            subs = sub.json()

            try:
                user = User.objects.get(email=flw_customer_email)
                user.subscription.status = subs['data'][0]['status']
                user.subscription.save()
            except User.DoesNotExist:
                return HttpResponse("User Does not exist", status=status.HTTP_400_BAD_REQUEST)



    return HttpResponse(status=status.HTTP_200_OK)