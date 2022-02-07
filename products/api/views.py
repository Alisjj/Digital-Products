from products.models import Course, Lesson
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import DigitalProduct
from .serializers import DigitalProductSerializer
from django.http import Http404
from rest_framework import permissions, status


class DigitalProductView(generics.ListCreateAPIView):
    serializer_class = DigitalProductSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = DigitalProduct.objects.filter(user=user)
        return queryset

class DigitalProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DigitalProductSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = DigitalProduct.objects.filter(user=user)
        return queryset