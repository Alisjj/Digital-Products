from django.db import models
import os

# User = get_user_model()
# User = 'alsajjad'

class Category(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class UploadFile(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    file = models.FileField(upload_to="media")

    def __str__(self):
        return "{}".format(os.path.basename(self.file.name))



class Product(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    cover = models.ForeignKey(UploadFile, related_name="product_image",on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=230)
    description = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='digital_products')
    content = models.ForeignKey(UploadFile, related_name="product_file", on_delete=models.SET_NULL, null=True, blank=True)
    content_url = models.URLField(null=True, blank=True)



    price = models.IntegerField(default=0)
    original_price = models.IntegerField(default=0, null=True, blank=True)
    preoder_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name



class Course(Product):
        preview_video = models.ForeignKey(UploadFile, on_delete=models.SET_NULL, null=True, blank=True)

class Section(models.Model):
    name =  models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sections")

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=120)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="lessons")

    def __str__(self):
        return self.name

class LessonDetail(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name="lesson_detail")
    file = models.ForeignKey(UploadFile, on_delete=models.SET_NULL, null=True, blank=True)
    file_url = models.URLField(blank=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.lesson.name

