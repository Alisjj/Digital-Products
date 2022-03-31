from itertools import product
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


urlpatterns = [
    path('<int:pk>/', views.ProductDetailView.as_view(), name = 'product-detail'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name = 'product-detail'),
    path('<int:pk>/delete/', views.ProductDestroy.as_view(), name = 'product-detail'),
    path('purchased-products/', views.PurchasedProductsView.as_view(), name='purchased-product'),
    path('course-list/', views.CourseList.as_view(), name="course-list"),
    path('course-create/', views.CourseView.as_view(), name="course-create"),
    path('course/<int:pk>/', views.CourseRetrieve.as_view(), name="course-retrieve"),
    path('course/<int:course_id>/sections/', views.CourseDetail.as_view(), name="course_detail"),
    path('course/<int:course_id>/sections/<int:section_id>/', views.SectionDetailView.as_view(), name="section_detail"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
