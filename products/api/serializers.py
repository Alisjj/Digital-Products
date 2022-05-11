from rest_framework import serializers
from products.models import Lesson, Product, Section
from products.models import Course

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'product_type',
            'cover',
            'category',
            'content',
            'content_url',
            'price',
            'original_price',
            'preoder_date',
        )

class PurchasedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
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

class CourseSerializer(serializers.ModelSerializer):

    # pricing_tiers = serializers.ListField()
    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'description',
            'cover',
            'category',
            'price',
            'original_price',
            'preoder_date',
            'preview_video',
        )
        
class LessonDetailSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Lesson
        fields = ("__all__")

class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ("__all__")