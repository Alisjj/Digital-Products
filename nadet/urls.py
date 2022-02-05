from django.contrib import admin
from django.urls import path, include
# from dj_rest_auth.registration.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('cont/', include('django.contrib.auth.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('products/', include('products.api.urls')),
]
