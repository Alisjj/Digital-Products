from . import views
from django.urls import path

urlpatterns = [
    path('courses/', views.CourseListApiView.as_view()),
    path('courses/<int:pk>/', views.CourseDetailApiView.as_view()),
    path('courses/create/', views.CourseCreateApiView.as_view()),
    path('courses/<int:pk>/update/', views.CourseUpdateApiView.as_view()),
    path('courses/<int:pk>/delete/', views.CourseDeleteApiView.as_view()),
    path('ebook/', views.EbookListApiView.as_view()),
    path('ebook/create/', views.EbookCreateApiView.as_view()),
    path('ebook/<int:pk>/', views.EbookDetailApiView.as_view()),
    path('ebook/<int:pk>/update/', views.EbookUpdateApiView.as_view()),
    path('ebook/<int:pk>/delete/', views.EbookDeleteApiView.as_view()),
    path('lesson/', views.LessonListApiView.as_view()),
    path('lesson/create/', views.LessonCreateApiView.as_view()),
    path('lesson/<int:pk>/', views.LessonDetailApiView.as_view()),
    path('lesson/<int:pk>/update/', views.LessonUpdateApiView.as_view()),
    path('lesson/<int:pk>/delete/', views.LessonDeleteApiView.as_view()),

]
