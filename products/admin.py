from django.contrib import admin

from products.models import Category, Course, Ebook, Lesson, User


admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Ebook)
admin.site.register(User)

