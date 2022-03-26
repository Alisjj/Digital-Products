from rest_framework import serializers
from subscription.models import Pricing


class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'