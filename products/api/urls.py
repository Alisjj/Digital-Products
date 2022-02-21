from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


urlpatterns = [
    path("digital-products/", views.DigitalProductListView.as_view()),
    path("digital-products/create/", views.DigitalProductCreateView.as_view()),
    path("digital-products/<int:pk>/", views.DigitalProductDetail.as_view()),
    path("digital-products/<int:pk>/update/", views.DigitalProductUpdate.as_view()),
    path("digital-products/<int:pk>/delete/", views.DigitalProductDestory.as_view()),
    path("categories/", views.CategoryView.as_view()),
    path("categories/<int:pk>/", views.CategoryDetail.as_view()),
    path("tickets/", views.TicketListView.as_view()),
    path("tickets/create/", views.TicketCreateView.as_view()),
    path("tickets/<int:pk>/", views.TicketDetail.as_view()),
    path("tickets/<int:pk>/update/", views.TicketUpdate.as_view()),
    path("tickets/<int:pk>/delete/", views.TicketDestroy.as_view()),
    path("services/", views.ServiceListView.as_view()),
    path("services/create/", views.ServiceCreateView.as_view()),
    path("services/<int:pk>/", views.ServiceDetail.as_view()),
    path("services/<int:pk>/update/", views.ServiceUpdate.as_view()),
    path("services/<int:pk>/delete/", views.ServiceDestroy.as_view()),
    path("courses/", views.CourseListView.as_view()),
    path("courses/create/", views.CourseCreateView.as_view()),
    path("courses/<int:pk>/", views.CourseDetail.as_view()),
    path("courses/<int:pk>/update/", views.CourseUpdate.as_view()),
    path("courses/<int:pk>/delete/", views.CourseDetail.as_view()),
    path("courses/sections/", views.SectionView.as_view(), name="section_list"),
    path("courses/sections/<int:pk>/", views.SectionEdit.as_view(), name="section_edit"),
    path("courses/sections/lessons/", views.LessonView.as_view(), name="lesson_list"),
    path("courses/sections/lessons/<int:pk>/", views.LessonEditView.as_view(), name="lesson_edit"),
    path("courses/sections/lessons/lesson-detail", views.LessonDetailView.as_view(), name="lesson-detail-list"),
    path("courses/sections/lessons/lesson-detail/<int:pk>/", views.LessonDetailEditView.as_view(), name="lesson-detail-edit"),
    path("files/", views.UploadFileView.as_view()),
    path("files/<int:pk>/", views.UploadFileDetailView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
