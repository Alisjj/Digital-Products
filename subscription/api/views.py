import os
import json
from django.http import JsonResponse
from rave_python import Rave
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import PricingSerializer, LoginReceiverSerializer
from subscription.models import Pricing
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

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

    except User.DoesNotExist:
        return JsonResponse({"details": "User does not exist"}, status=401)

    return JsonResponse({"details": "Successful"}, status=200)
