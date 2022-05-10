from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('available', 'created', 'updated')

class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'image', 'description')