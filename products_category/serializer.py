from rest_framework import serializers
from .models import Categories, Product, ProductReview

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
    
class ProductSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = "__all__"