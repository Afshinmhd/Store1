from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductViewSerializer
from .models import Product
from common.pagination import CustomPagination
from django.shortcuts import get_object_or_404
from rest_framework import status
from .permissions import IsOwnOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnOrReadOnly]
    pagination_class = CustomPagination
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


""" 
  def get_serializer(self, request):
        if self.action in ['list', 'retrieve']:
            return ProductViewSerializer
        else:
            return ProductSerializer
            """
