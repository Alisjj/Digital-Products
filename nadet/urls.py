from django.contrib import admin
from django.urls import path, include
from users.api.views import PasswordResetConfirmView
from products.api.views import ProductListView, UserProductListView, ProductCreateView, flw_webhook
from subscription.api.views import PricingView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls')),
    path('change-password/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
    path('auth/', include('users.api.urls')),
    path('ps/', include('products.api.urls')),


    path('discover/', ProductListView.as_view(), name="discover"),
    path('products/', UserProductListView.as_view(), name="user-products"),
    path('products/create/', ProductCreateView.as_view(), name="product-create"),
    path('pricing/', PricingView.as_view(), name="pricing"),

    path('webhooks/flutterwave/', flw_webhook),


]
