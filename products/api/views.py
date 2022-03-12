from products.models import Category, Course, Lesson, LessonDetail, Product, UploadFile
from rest_framework import generics
from .serializers import CategorySerializer, CourseSerializer, ProductSerializer
from rest_framework import permissions

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


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(active=True)

class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class UserProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

class ProductDestroy(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

