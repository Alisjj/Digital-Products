from products.models import Category, Course, Lesson, LessonDetail, Product, UploadFile
from django.contrib.auth import get_user_model

from django.http import HttpResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CategorySerializer, CourseSerializer, ProductSerializer, TransactionSerializer
from django.conf import settings
from rave_python import Rave

User = get_user_model()
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

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class PaymentView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = TransactionSerializer

    def post(self, request):
        payload = request.data
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


# class FlwWebhookView(View):
#     permission_classes = (permissions.AllowAny,)

    
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
            "Authorization": settings.FLW_SECRET_KEY
            })

        resp = res.json()

        product_id = resp['data']['meta']['product_id']
        flw_customer_email = resp['data']['customer']['email']
        try:
            user = User.objects.get(email=flw_customer_email)
            user.userlibrary.products.add(product_id)
        except User.DoesNotExist:
            #TODO: Anonymous
            print("User does not exist")
            pass

    return HttpResponse(status=status.HTTP_200_OK)