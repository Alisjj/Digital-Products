from rest_framework import serializers
from products.models import Category, Course, Lesson, LessonDetail, Product, Section, Transaction, UploadFile


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


class CustomerSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phonenumber = serializers.CharField()
    name = serializers.CharField(max_length=100)


# class MetaSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     name = serializers.CharField(max_length=100)

class TransactionSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer()
    redirect_url = serializers.URLField()


    class Meta:
        model = Transaction
        fields = (
            "tx_ref",
            "amount",
            "currency",
            "redirect_url",
            "customer",

        )

        

