from rest_framework import serializers
from subscription.models import Pricing


class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'

class CancelSubscriptionSerializer(serializers.Serializer):
    username = serializers.CharField()
    plan_id = serializers.CharField()

    class Meta:
        fields = (
            'username',
            'plan_id'
        )

class PaymentVerificationSerializer(serializers.Serializer):
    transaction_id = serializers.CharField()

    class Meta:
        fields = (
            'transaction_id'
        )