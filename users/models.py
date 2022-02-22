from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
class User(AbstractUser):
    profile_pic = models.ImageField()
    full_name = models.CharField(max_length=120)
    bio = models.TextField()
    facebook_url = models.URLField(max_length=150)
    twitter_url = models.URLField(max_length=150)
    profile_link = models.URLField(max_length=150)
    referral_url = models.URLField(max_length=150)

