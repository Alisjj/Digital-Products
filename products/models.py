from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Course(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.TextField()
    cover_image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    video_file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title


class Ebook(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.TextField()
    cover_image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

