from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from products.models import Product, Course

class User(AbstractUser):
    profile_pic = models.ImageField()
    full_name = models.CharField(max_length=120)
    bio = models.TextField()
    facebook_url = models.URLField(max_length=150)
    twitter_url = models.URLField(max_length=150)
    profile_link = models.URLField(max_length=150)
    referral_url = models.URLField(max_length=150)


class UserLibrary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Product, blank=True)
    # courses = models.ManyToManyField(Course, blank=True, related_name="courses")

    class Meta:
        verbose_name_plural = "UserLibraries"

    def __str__(self):
        return self.user.email

def post_save_user_library(sender, instance, created, **kwargs):
    if created:
        UserLibrary.objects.create(user=instance)

post_save.connect(post_save_user_library, sender=User)