from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


urlpatterns = [
    path("digital-product/", views.DigitalProductView.as_view()),
    path("digital-product/<int:pk>/", views.DigitalProductDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
