from rest_framework import serializers
from .models import OrderItem, Order


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('quantity',)

class CartOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'