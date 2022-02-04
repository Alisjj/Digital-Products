from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    profile_pic = models.ImageField()
    bio = models.TextField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    profile_url = models.URLField(blank=True, null=True)
    referral_url = models.URLField(blank=True, null=True)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
