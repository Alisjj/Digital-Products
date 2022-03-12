from rest_framework import serializers
from products.models import Category, Course, Lesson, LessonDetail, Section, UploadFile


class CategorySerializer(serializers.ModelSerializer):
    courses = serializers.StringRelatedField(many=True, read_only=True)
    tickets = serializers.StringRelatedField(many=True, read_only=True)
    digital_products = serializers.StringRelatedField(many=True, read_only=True)
    services = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = (
            'user',
            'name',
            'courses',
            'tickets',
            'digital_products',
            'services',
        )


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class Course(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    lessons = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Section
        fields = (
            'pk',
            'name',
            'course',
            'lessons',
        )


class LessonSerializer(serializers.ModelSerializer):
    lesson_detail = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Lesson
        fields = (
            'pk',
            'name',
            'section',
            'lesson_detail',
        )


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonDetail
        fields = '__all__'