from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction

class CustomRegistration(RegisterSerializer):
    full_name = serializers.CharField(max_length=120)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.full_name = self.data.get('full_name')
        user.save()
        return user
    