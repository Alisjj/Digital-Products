from products.models import Category, Course, Lesson, Service, Ticket
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import DigitalProduct
from .serializers import CategorySerializer, DigitalProductSerializer, ServiceSerializer, TicketSerializer
from django.http import Http404
from rest_framework import permissions, status


class CatgoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Category.objects.filter(user=user)
        return queryset


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Category.objects.filter(user=user)
        return queryset

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

class TicketView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Ticket.objects.filter(user=user)
        return queryset

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Ticket.objects.filter(user=user)
        return queryset

class ServiceView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Service.objects.filter(user=user)
        return queryset

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Service.objects.filter(user=user)
        return queryset
