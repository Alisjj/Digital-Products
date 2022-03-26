from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import PricingSerializer
from subscription.models import Pricing

class PricingView(generics.ListAPIView):
    serializer_class = PricingSerializer
    permission_classes = (AllowAny, )
    queryset = Pricing.objects.all()