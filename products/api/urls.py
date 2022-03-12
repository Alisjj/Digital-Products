from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


urlpatterns = [
    path("courses/", views.CourseListView.as_view()),
    path("courses/create/", views.CourseCreateView.as_view()),
    path("courses/<int:pk>/", views.CourseDetail.as_view()),
    path("courses/<int:pk>/update/", views.CourseUpdate.as_view()),
    path("courses/<int:pk>/delete/", views.CourseDetail.as_view()),
    path("files/", views.UploadFileView.as_view()),
    path("files/<int:pk>/", views.UploadFileDetailView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
