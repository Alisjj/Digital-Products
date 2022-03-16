from django.contrib import admin
from django.urls import path, include
from users.api.views import PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('change-password/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
    path('auth/', include('users.api.urls')),
    path('products/', include('products.api.urls')),
    path('subscriptions/', include('subscriptions.api.urls')),
]
