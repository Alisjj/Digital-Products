from itertools import product
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


urlpatterns = [
    path('<int:id>/', views.ProductDetailView.as_view(), name = 'product_detail')

]

urlpatterns = format_suffix_patterns(urlpatterns)
