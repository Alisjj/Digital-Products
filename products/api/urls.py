from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


urlpatterns = [
    path("digital-products/", views.DigitalProductView.as_view()),
    path("digital-product/<int:pk>/", views.DigitalProductDetail.as_view()),
    path("categories/", views.CatgoryView.as_view()),
    path("category/<int:pk>/", views.CategoryDetail.as_view()),
    path("tickets/", views.TicketView.as_view()),
    path("ticket/<int:pk>/", views.TicketDetail.as_view()),
    path("service/", views.ServiceView.as_view()),
    path("ticket/<int:pk>/", views.ServiceDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
