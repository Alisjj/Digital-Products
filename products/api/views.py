# from lib2to3.pgen2.tokenize import TokenError
import os
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from products.models import Course, ImageUpload, Product, Section
from django.contrib.auth import get_user_model
import requests
from django.http import HttpResponse
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
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    


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
    parser_classes = [FormParser, MultiPartParser]
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        # file_obj = dict((request.data).lists())['cover']
        images = request.FILES.getlist('cover_images')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.data['product_type'] == "subscription":
            if request.user.subscription.pricing.name == "Free":
                return Response("Upgrade your pricing plan to create a subscription service", status=status.HTTP_401_UNAUTHORIZED)
        i = serializer.save(user=request.user)
        self.perform_create(i)
        for image in images:
            ImageUpload.objects.create(product=i, image=image)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CourseView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    #     return super().perform_create(serializer)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user_courses = Course.objects.filter(user=user)
        user_subscription = user.subscription.pricing.name
        if user_subscription == "Free" and user_courses.count() == 5:
            return Response({"details": "Upgrade your Subscription Plan to add a course"}, status=status.HTTP_401_UNAUTHORIZED)
        elif user_subscription == "Basic Plan" and user_courses.count() == 20:
            return Response({"details": "Upgrade your Subscription Plan to add a course"}, status=status.HTTP_401_UNAUTHORIZED)
        elif user_subscription == "Pro Plan" and user_courses.count() == 30:
            return Response({"details": "Upgrade your Subscription Plan to add a course"}, status=status.HTTP_401_UNAUTHORIZED)
        self.perform_create(serializer.save(user=user))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class PurchasedCourseList(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.request.user.userlibrary.courses.all()

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