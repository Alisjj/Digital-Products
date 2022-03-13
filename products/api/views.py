from products.models import Category, Course, Lesson, LessonDetail, Product, UploadFile
import requests
import json
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CategorySerializer, CourseSerializer, ProductSerializer, TransactionSerializer
from django.conf import settings
from rave_python import Rave

rave = Rave(settings.FLW_PUBLIC_KEY, settings.FLW_SECRET_KEY, usingEnv=False )

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

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class PaymentView(generics.GenericAPIView):

    serializer_class = TransactionSerializer

    def post(self, request):
        payload = request.data
        print()
        data = {
            "tx_ref": payload['tx_ref'],
            "amount": payload['amount'],
            "currency": payload['currency'],
            "redirect_url": payload['redirect_url'],
            "customer": {
                "email": payload['customer.email'],
                "phonenumber": payload['customer.phonenumber'],
                "name": payload['customer.name'],
            }
        }
        
        res = requests.post("https://api.flutterwave.com/v3/payments", json=data, headers={
            "Authorization": settings.FLW_SECRET_KEY
            })

        return Response(res.json())


# class TransactionView(generics.GenericAPIView)