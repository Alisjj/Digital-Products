from django.db import models
from django.contrib.auth.models import AbstractUser
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(models.Model):
    pass

