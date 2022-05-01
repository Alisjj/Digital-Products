import os
import requests
import json
from django.conf import settings
from rest_framework.response import Response
from django.http import JsonResponse
from rave_python import Rave
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from .serializers import CancelSubscriptionSerializer, PaymentVerificationSerializer, PricingSerializer
from subscription.models import Pricing
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from subscription.models import CustomPricing
from products.models import Product

rave = Rave(os.getenv('FLW_PUBLIC_KEY'), os.getenv('RAVE_SECRET_KEY'))
User = get_user_model()

class PricingView(generics.ListAPIView):
    serializer_class = PricingSerializer
    permission_classes = (AllowAny, )
    queryset = Pricing.objects.all()


@csrf_exempt
def login_receiver(request, *args, **kwargs):
    object = json.loads(request.body)
    email = object['email']
    try:
        user = User.objects.get(email=email)
        subscription = user.subscription
        if subscription.pricing.name != "Free":
            sub = rave.Subscriptions.fetch(subscription.flw_subscription_id)
            subscription.status = sub['returnedData']['data']['plansubscriptions'][0]['status']
            subscription.save()
        print(subscription.status)

    except User.DoesNotExist:
        return JsonResponse({"details": "User does not exist"}, status=401)

    return JsonResponse({"details": "Successful"}, status=200)

class PaymentVerification(generics.GenericAPIView):
    serializer_class =  PaymentVerificationSerializer
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        tr_id = request.data['transaction_id']
        url = "https://api.flutterwave.com/v3/transactions/{}/verify".format(tr_id)
        res = requests.get(url=url, headers={
            "Authorization": settings.RAVE_SECRET_KEY
            })
        resp = res.json()
        try:
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
                    print("Upgrade Successfull")
                except User.DoesNotExist:
                    return Response("User Does not exist", status=status.HTTP_400_BAD_REQUEST)


            if event_type == "product.checkout":
                product_id = resp['data']['meta']['product_id']
                product = Product.objects.get(id=product_id)
                flw_customer_email = resp['data']['customer']['email']
                try:
                    user = User.objects.get(email=flw_customer_email)
                    if product.preoder_date is not None:
                        product.waitlist.users.add(user.id)
                    user.userlibrary.products.add(product_id)
                    print("product added")
                except User.DoesNotExist:
                    return Response("User Does not exist", status=status.HTTP_400_BAD_REQUEST)

            if event_type == "course.checkout":
                course_id = resp['data']['meta']['course_id']
                flw_customer_email = resp['data']['customer']['email']
                try:
                    user = User.objects.get(email=flw_customer_email)
                    user.userlibrary.courses.add(course_id)
                    print("Course Added")
                except User.DoesNotExist:
                    return Response("User Does not exist", status=status.HTTP_400_BAD_REQUEST)
            return Response({"details": "Successfull"}, status=200)
        except Exception as e:
            return Response({"datails": "transaction not found",
                            "error": "{}".format(e)}, status=status.HTTP_400_BAD_REQUEST)

class CancelSubscription(generics.GenericAPIView):
    serializer_class = CancelSubscriptionSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        flw_customer_email = request.data["email"]
        plan_id = request.data["plan_id"]
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
            return Response({"details":"User Does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"details": "Subscription Cancel Successfull"}, status=status.HTTP_200_OK)

class CreatePricingPlan(generics.GenericAPIView):
    serializer_class = PricingSerializer

    def post(self, request):
        name = request.data['name']
        amount = request.data['amount']
        currency = request.data['currency']
        duration = request.data['duration']
        interval = request.data['interval']

        payload = {
            "name": name,
            "amount": amount,
            "currency": currency,
            "duration": duration,
            "interval": interval
        }

        url = "https://api.flutterwave.com/v3/payment-plans"

        try:
            plan = requests.post(url=url, headers={
            "Authorization": settings.RAVE_SECRET_KEY
            }, json=payload)

        except Exception as e:
            return Response({"details": "Plan Creation Failed {}".format(e) }, status=status.HTTP_400_BAD_REQUEST)

        name = plan['data']['name']
        plan_id = plan['data']['id']
        amount = plan['data']['amount']
        currency = plan['data']['currency']
    # currency

        CustomPricing.objects.create(user=request.user, plan_id=plan_id, name=name, currency=currency)

        return Response({"details": "Pricing Tier Created Successfully"}, status=status.HTTP_201_CREATED)

