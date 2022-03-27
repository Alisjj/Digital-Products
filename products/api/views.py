# from lib2to3.pgen2.tokenize import TokenError
import os
from subprocess import check_output
from products.models import Category, Course, Lesson, LessonDetail, Product, UploadFile
from django.contrib.auth import get_user_model
from rest_framework import mixins
import requests
from django.http import HttpResponse
from products.mixins import CourseAccesMixin
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics

from subscription.models import Pricing
from .serializers import CategorySerializer, CourseSerializer, ProductSerializer, TransactionSerializer, PurchasedProductSerializer
from django.conf import settings
from rave_python import Rave

User = get_user_model()
rave = Rave(os.getenv('FLW_PUBLIC_KEY'), os.getenv('RAVE_SECRET_KEY'))

class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Category.objects.filter(user=user)
        return queryset


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Category.objects.filter(user=user)
        return queryset


class ProductListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(active=True)

class ProductDetailView(generics.RetrieveAPIView):
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
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class CourseView(CourseAccesMixin, generics.ListCreateAPIView  ):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

        
        
    
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
            params = {
                "email": flw_customer_email,
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

    return HttpResponse(status=status.HTTP_200_OK)