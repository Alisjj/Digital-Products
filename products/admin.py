from telnetlib import SE
from django.contrib import admin
from .models import (
    Course, ImageUpload, Lesson, Product, Section, Waitlist
    )

admin.site.register(Product)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(Waitlist)
admin.site.register(ImageUpload)