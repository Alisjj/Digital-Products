import os
from unicodedata import name
from rave_python import Rave, RaveExceptions
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from subscriptions.models import Membership
from .serializers import MembershipSerializer
from django.shortcuts import get_object_or_404
from users.models import User

rave = Rave(os.getenv("FLW_PUBLIC_KEY"), os.getenv("FLW_SECRET_KEY"), os.getenv("FLW_ENCRYPTION_KEY"))


Basic_Plan_Monthly = rave.Subscription.create({
    "name": "Basic Plan Monthly",
    "amount": 29,
    "interval": "Monthly",
    "currency": "USD",
})

Basic_Plan_Yearly = rave.Subscription.create({
    "name": "Basic Plan Yearly",
    "amount": 313,
    "interval": "Yearly",
    "currency": "USD",
})

Pro_Plan_Monthly = rave.Subscription.create({
    "name": "Pro Plan Monthly",
    "amount": 49,
    "interval": "Monthly",
    "currency": "USD",
})

Pro_Plan_Yearly = rave.Subscription.create({
    "name": "Pro Plan Yearly",
    "amount": 529,
    "interval": "Yearly",
    "currency": "USD",
})

Premium_Plan_Monthly = rave.Subscription.create({
    "name": "Premium Plan Monthly",
    "amount": 99,
    "interval": "Monthly",
    "currency": "USD",
})

Premium_Plan_Yearly = rave.Subscription.create({
    "name": "Premium Plan Yearly",
    "amount": 1069,
    "interval": "Yearly",
    "currency": "USD",
})

  

@require_POST
@csrf_exempt
def init_membership(request):
    secret_hash = os.getenv("FLW_SECRET_HASH")
    signature = request.headers.get("verifi-hash")
    if signature == None or (signature != secret_hash):
        return Response("Not from flutterwave", status=401)
    payload = request.body
    try:
        transanction = rave.Subscriptions.fetchSubscription(payload.data.id)
        if payload.data.status == "successful" and payload.data.amount == transanction.data.amount and payload.data.currency == transanction.data.currency:
            Membership = Membership.objects.create(
                user = get_object_or_404(User, email=transanction.data.customer.email),
                interval = transanction.data.interval,
                started = transanction.data.createdAt,
                plan_id = transanction.data.id,
                active = True
            )
            return Response("Payment successful", status=200)
        else:
            return Response("Payment failed", status=400)
    except RaveExceptions.PlanStatusError as e:
        print(e.err["errMsg"])
        print(e.err["flwRef"])
        return Response("Payment failed", status=400)


@require_POST
@csrf_exempt
def cancel_membership(request):
    user_membership = get_object_or_404(Membership, user=request.user, active=True)
    membership_plan_id = user_membership.plan_id
    try:
        subscription = rave.cancelSubscription(membership_plan_id)
        if subscription:
            user_membership = Membership.objects.update(
                interval="Cancelled",
                active=False,
                started = "Cancelled",
                plan_id="Cancelled",
            )
            return Response("Membership cancelled", status=200)
        else:
            return Response("Subscription not found", status=400)
    except RaveExceptions.PlanStatusError as e:
        print(e.err["errMsg"])
        print(e.err["flwRef"])
        return Response("Payment failed", status=400)


    