from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction

from users.models import User

class CustomRegistration(RegisterSerializer):
    full_name = serializers.CharField(max_length=120)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.full_name = self.data.get('full_name')
        user.save()
        return user

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'email',
            'profile_pic',
            'full_name',
            'bio',
            'facebook_url',
            'twitter_url',
            'profile_link',
            'referral_url',
        )
        read_only_fields = ('pk', 'email', 'profile_link', 'referral_url')
    