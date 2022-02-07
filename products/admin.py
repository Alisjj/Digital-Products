from telnetlib import SE
from django.contrib import admin
from .models import (
    Category, Uploads, UploadFile, Variant, 
    DigitalProduct, Ticket, Service, Course, Section, Lesson, 
    LessonDetail, PreviewVideo)

admin.site.register(Category)
admin.site.register(Uploads)
admin.site.register(UploadFile)
admin.site.register(Variant)
admin.site.register(DigitalProduct)
admin.site.register(Ticket)
admin.site.register(Service)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(LessonDetail)
admin.site.register(PreviewVideo)