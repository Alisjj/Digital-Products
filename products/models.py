from django.db import models
from django.db.models.signals import post_save

PRODUCT_TYPE = [
    ('digital', 'Digital Product'),
    ('ticket', 'Ticket'),
    ('service', 'Service'),
    ('subscription', 'Subscription')
]
class ImageUpload(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()

    def __str__(self):
        return self.image.name

class Product(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=230)
    product_type = models.CharField(choices=PRODUCT_TYPE, max_length=15)
    description = models.TextField()

    content = models.FileField(null=True, blank=True)
    pricing_tier = models.ManyToManyField('subscription.CustomPricing', blank=True)
    content_url = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=120)
    active = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=4)
    original_price = models.IntegerField(default=0, null=True, blank=True)
    preoder_date = models.DateTimeField(null=True, blank=True)
    quantity = models.PositiveBigIntegerField(null=True, blank=True)
    downloadable_file = models.BooleanField(default=True)
    redirect_url = models.URLField()

    
    def __str__(self):
        return self.name

class Waitlist(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="waitlist")
    users = models.ManyToManyField('users.User', related_name="users")

    def __str__(self):
        return self.product.name


class Course(Product):
    preview_video = models.FileField(null=True, blank=True)

class Section(models.Model):
    name =  models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sections")

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=120)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="lessons")
    file = models.FileField(null=True, blank=True)
    file_url = models.URLField(blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

def post_save_waitlist(sender, instance, created, **kwargs):
    if instance.preoder_date is not None:
        if created:
            Waitlist.objects.create(product=instance)

post_save.connect(post_save_waitlist, sender=Product)