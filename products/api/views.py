from products.models import Category, Course, Lesson, LessonDetail, UploadFile
from rest_framework import generics
from .serializers import CategorySerializer, CourseSerializer, LessonDetailSerializer, LessonSerializer,  UploadFileSerializer
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
    


class LessonView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDetailView(generics.ListCreateAPIView):
    serializer_class = LessonDetailSerializer
    queryset = LessonDetail.objects.all()

class LessonDetailEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonDetailSerializer
    queryset = LessonDetail.objects.all()