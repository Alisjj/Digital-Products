import os
from rave_python import Rave
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
rave = Rave(os.getenv('FLW_PUBLIC_KEY'), os.getenv('RAVE_SECRET_KEY'))

class Pricing(models.Model):
    name = models.CharField(max_length=100)
    plan_id = models.CharField(max_length=100)

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

def post_save_user(sender, instance, created, *args, **kwargs):
    if created:
        free = Pricing.objects.get(name="Free")
        Subscription.objects.create(user=instance, pricing=free)

def user_logged_in_receiver(sender, user, request, **kwargs):
    subscription = user.subscription
    print(subscription)
    if subscription.pricing.name != "Free":
        sub = rave.Subscriptions.fetch(subscription.flw_subscription_id)
        subscription.status = sub['returnedData']['data']['plansubsptions'][0]['status']


user_logged_in.connect(user_logged_in_receiver)
post_save.connect(post_save_user, sender=User)
