from django.urls import path, include
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('verify-email', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    
    # path('products/', include('products.api.urls')),
]
