from rest_framework.serializers import ModelSerializer
from subscriptions.models import Membership

#create 
class MembershipSerializer(ModelSerializer):
    class Meta:
        model = Membership
        fields = ['user', 'interval', 'started', 'active']