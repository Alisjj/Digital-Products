from django.db import models
from users.models import User
import os


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class UploadFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="media")

    def __str__(self):
        return "{}".format(os.path.basename(self.file.name))



class DigitalProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(UploadFile, related_name="product_image",on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=230)
    price = models.IntegerField(default=0)
    original_price = models.IntegerField(default=0, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    preoder_date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.ForeignKey(UploadFile, related_name="product_file", on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(UploadFile, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=230)
    price = models.IntegerField(default=0)
    original_price = models.IntegerField(default=0, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)   
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(UploadFile, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=230)
    price = models.IntegerField(default=0)
    original_price = models.IntegerField(default=0, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(UploadFile, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=230)
    price = models.IntegerField(default=0)
    original_price = models.IntegerField(default=0, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    preorder_date = models.DateTimeField(null=True, blank=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Section(models.Model):
    name =  models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=120)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class LessonDetail(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    file = models.ForeignKey(UploadFile, on_delete=models.SET_NULL, null=True, blank=True)
    file_url = models.URLField(blank=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.lesson.name

class PreviewVideo(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.ForeignKey(UploadFile, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.file
