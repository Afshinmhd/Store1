from .cart import Cart
from home.models import Product
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import CartSerializer, CartOrderSerializer
from .models import Order, OrderItem
from accounts.models import User


class CartAddViewSet(viewsets.ViewSet):
     def create(self, request):
         cart = Cart(request)
         product = get_object_or_404(Product, pk=1)
         ser_data = CartSerializer(data=request.data)
         ser_data.is_valid(raise_exception=True)
         cart.add(product, ser_data.validated_data['quantity'])
         return Response(status=status.HTTP_201_CREATED)

class OrderCreateViewSet(viewsets.ViewSet):
    def list(self, request, pk=None):
        cart = Cart(request)
        order = Order.objects.create(user=User.objects.get(is_admin=True))
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=float(item['price']), quantity=item['quantity'])
        return Response(status=status.HTTP_200_OK)

class OrderDetailViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        order = get_object_or_404(Order, id=pk)
        ser_data = CartOrderSerializer(instance=order)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)



        
