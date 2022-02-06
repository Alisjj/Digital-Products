from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('cont/', include('django.contrib.auth.urls')),
    path('auth/', include('users.api.urls')),
    # path('products/', include('products.api.urls')),
]
