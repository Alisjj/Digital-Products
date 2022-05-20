from rest_framework import serializers
from products.models import CourseImageUpload, ImageUpload, Lesson, Product, Section
from products.models import Course

class ProductSerializer(serializers.ModelSerializer):

    cover_images = serializers.ImageField(read_only=True)
    images = serializers.SerializerMethodField(source='get_images')
    
    def get_images(self, product):
        arr = []
        images = product.images.all()
        for image in images:
            arr.append('http://localhost:8000' + str(image.image.url))
        return arr

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'product_type',
            'images',
            'cover_images',
            'category',
            'content',
            'content_url',
            'price',
            'original_price',
            'preoder_date',
            'quantity',
            'downloadable_file',
            'redirect_url',
        )

class PurchasedProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'category',
            'content',
            'content_url',
            'price',
            'original_price',
            'preoder_date',
            
        )

class CourseSerializer(serializers.ModelSerializer):

    cover_images = serializers.ImageField(read_only=True)
    images = serializers.SerializerMethodField(source='get_images')
    
    def get_images(self, course):
        arr = []
        images = course.course_images.all()
        for image in images:
            arr.append('http://localhost:8000' + str(image.image.url))
        return arr

    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'description',
            'cover_images',
            'images',
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

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageUpload
        fields = (
            'product',
            'image',
        )

class CourseImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseImageUpload
        fields = (
            'course',
            'image',
        )

class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ("__all__")