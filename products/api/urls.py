from itertools import product
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


urlpatterns = [
    path('<int:pk>/', views.ProductDetailView.as_view(), name = 'product-detail'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name = 'product-detail'),
    path('<int:pk>/delete/', views.ProductDestroy.as_view(), name = 'product-detail'),
    path('pay/', views.PaymentView.as_view())
    

]

urlpatterns = format_suffix_patterns(urlpatterns)
