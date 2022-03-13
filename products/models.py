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
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="products")
    cover = models.ForeignKey(UploadFile, related_name="product_image",on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=230)
    description = models.TextField()

    content = models.ForeignKey(UploadFile, related_name="product_file", on_delete=models.SET_NULL, null=True, blank=True)
    content_url = models.URLField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='digital_products')


    active = models.BooleanField(default=False)
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



class Transaction(models.Model):
    """Represents a transaction for a specific payment type and user"""
    user = models.ForeignKey(
        "users.User", related_name="flw_transactions", on_delete=models.CASCADE
    )
    created_datetime = models.DateTimeField(auto_now_add=True)
    tx_ref = models.CharField(max_length=100)
    flw_ref = models.CharField(max_length=100)
    device_fingerprint = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    currency = models.CharField(max_length=3)
    charged_amount = models.DecimalField(decimal_places=2, max_digits=9)
    app_fee = models.DecimalField(decimal_places=2, max_digits=9)
    merchant_fee = models.DecimalField(decimal_places=2, max_digits=9)
    processor_response = models.CharField(max_length=100)
    auth_model = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
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