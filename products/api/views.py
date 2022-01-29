from products.models import Course, Ebook, Lesson
from .serializers import CourseSerializer
from rest_framework import generics
from rest_framework import permissions

class CourseListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer

class CourseCreateApiView(generics.CreateAPIView):
    model = Course
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer

class CourseDetailApiView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer


class CourseUpdateApiView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer


class CourseDeleteApiView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer

class EbookListApiView(generics.ListAPIView):
    queryset = Ebook.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer

class EbookCreateApiView(generics.CreateAPIView):
    model = Ebook
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer

class EbookDetailApiView(generics.RetrieveAPIView):
    queryset = Ebook.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer


class EbookUpdateApiView(generics.UpdateAPIView):
    queryset = Ebook.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer


class EbookDeleteApiView(generics.DestroyAPIView):
    queryset = Ebook.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer


class LessonListApiView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer

class LessonCreateApiView(generics.CreateAPIView):
    model = Lesson
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer

class LessonDetailApiView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer


class LessonUpdateApiView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer


class LessonDeleteApiView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CourseSerializer
