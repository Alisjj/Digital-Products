from products.models import Category, Course, Lesson, Service, Ticket, UploadFile
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import DigitalProduct
from .serializers import CategorySerializer, CourseSerializer, DigitalProductSerializer, ServiceSerializer, TicketSerializer, UploadFileSerializer
from django.http import Http404
from rest_framework import permissions, status

class CategoryView(generics.ListCreateAPIView):
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

class DigitalProductListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = DigitalProductSerializer
    queryset = DigitalProduct.objects.all()

class DigitalProductCreateView(generics.CreateAPIView):
    serializer_class = DigitalProductSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = DigitalProduct.objects.filter(user=user)
        return queryset

class DigitalProductDetail(generics.RetrieveAPIView):
    serializer_class = DigitalProductSerializer
    queryset = DigitalProduct.objects.all()

class DigitalProductUpdate(generics.UpdateAPIView):
    serializer_class = DigitalProductSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = DigitalProduct.objects.filter(user=user)
        return queryset

class DigitalProductDestory(generics.DestroyAPIView):
    serializer_class = DigitalProductSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = DigitalProduct.objects.filter(user=user)
        return queryset

class TicketListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

class TicketCreateView(generics.CreateAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Ticket.objects.filter(user=user)
        return queryset

class TicketDetail(generics.RetrieveAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

class TicketUpdate(generics.UpdateAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Ticket.objects.filter(user=user)
        return queryset
class TicketDestroy(generics.DestroyAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Ticket.objects.filter(user=user)
        return queryset

    
class ServiceListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class ServiceCreateView(generics.CreateAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Service.objects.filter(user=user)
        return queryset

class ServiceDetail(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class ServiceUpdate(generics.UpdateAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Service.objects.filter(user=user)
        return queryset

class ServiceDestroy(generics.DestroyAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Service.objects.filter(user=user)
        return queryset


class CourseListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseCreateView(generics.CreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Course.objects.filter(user=user)
        return queryset

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Course.objects.filter(user=user)
        return queryset

class CourseUpdate(generics.UpdateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Course.objects.filter(user=user)
        return queryset
class CourseDestroy(generics.DestroyAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Course.objects.filter(user=user)
        return queryset


class UploadFileView(generics.ListCreateAPIView):
    serializer_class = UploadFileSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = UploadFile.objects.filter(user=user)
        return queryset

class UploadFileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UploadFileSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = UploadFile.objects.filter(user=user)
        return queryset
    
