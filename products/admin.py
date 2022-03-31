from telnetlib import SE
from django.contrib import admin
from .models import (
    Category, UploadFile,Product, Course, Section, Lesson)

admin.site.register(Category)
admin.site.register(UploadFile)
admin.site.register(Product)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lesson)