from rest_framework import serializers
from .models import ProductCart

class ProductCartSerializer(serializers.ModelSerializer):
    cart = serializers.SlugRelatedField(slug_field ='id', read_only=True, many=False)
    
    class Meta:
        model = ProductCart
        fields = ['id', 'cart', 'product', 'quantity']


class EditProductCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCart
        fields = ['id', 'cart', 'product', 'quantity']
        read_only_fields = ['id', 'cart', 'product']