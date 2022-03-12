from rest_framework import serializers
from products.models import Category, Course, Lesson, LessonDetail, Product, Section, UploadFile


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

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
                'name',
                'description',
                'cover',
                'category',
                'content',
                'content_url',
                'price',
                'original_price',
                'preoder_date',
        )

        

