from rest_framework import serializers
from .models import Product, ProductImage

class ProductDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth= 5

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
        verbose_name = 'Product image'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'





