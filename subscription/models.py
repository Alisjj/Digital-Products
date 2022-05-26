import os
from rave_python import Rave
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth import get_user_model
from allauth.account.signals import email_confirmed

User = get_user_model()
rave = Rave(os.getenv('FLW_PUBLIC_KEY'), os.getenv('RAVE_SECRET_KEY'))

class Pricing(models.Model):
    name = models.CharField(max_length=100)
    plan_id = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name="subscriptions")
    created = models.DateTimeField(auto_now_add=True)
    flw_subscription_id = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email


class CustomPricing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # course = models.ForeignKey(settings.AUTH_USER_MODE)
    plan_id = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=3)


class Transaction(models.Model):
    """Represents a transaction for a specific payment type and user"""
    user = models.ForeignKey(
        "users.User", related_name="flw_transactions", on_delete=models.CASCADE
    )
    created_datetime = models.DateTimeField(auto_now_add=True)
    tx_ref = models.CharField(max_length=100)
    flw_ref = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    currency = models.CharField(max_length=3)
    charged_amount = models.DecimalField(decimal_places=2, max_digits=9)
    app_fee = models.DecimalField(decimal_places=2, max_digits=9)
    merchant_fee = models.DecimalField(decimal_places=2, max_digits=9)
    narration = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(
        help_text="Created datetime received from Flutterwave"
    )
    account_id = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return self.tx_ref

def post_email_confirmed(request, email_address, *args, **kwargs):
    user = User.objects.get(email=email_address.email)
    free = Pricing.objects.get(name="Free")
    Subscription.objects.create(user=user, pricing=free)

email_confirmed.connect(post_email_confirmed)
