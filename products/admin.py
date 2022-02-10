from telnetlib import SE
from django.contrib import admin
from .models import (
    Category, UploadFile,DigitalProduct, 
    Ticket, Service, Course, Section, Lesson, 
    LessonDetail, PreviewVideo)

admin.site.register(Category)
admin.site.register(UploadFile)
admin.site.register(DigitalProduct)
admin.site.register(Ticket)
admin.site.register(Service)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(LessonDetail)
admin.site.register(PreviewVideo)