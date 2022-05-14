from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path


urlpatterns = [
    path('product-create/', views.ProductCreateView.as_view(), name = 'product-create'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name = 'product-detail'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name = 'product-update'),
    path('<int:pk>/delete/', views.ProductDestroy.as_view(), name = 'product-delete'),
    path('purchased-products/', views.PurchasedProductsView.as_view(), name='purchased-product'),
    path('purchased-courses/', views.PurchasedCourseList.as_view(), name='purchased-course'),
    path('course-list/', views.CourseList.as_view(), name="course-list"),
    path('course-create/', views.CourseView.as_view(), name="course-create"),
    path('course/<int:pk>/', views.CourseRetrieve.as_view(), name="course-retrieve"),
    path('course/<int:course_id>/sections/', views.CourseDetail.as_view(), name="course_detail"),
    path('course/<int:course_id>/sections/<int:section_id>/', views.SectionDetailView.as_view(), name="section_detail"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
