from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductViewSerializer
from .models import Product
from common.pagination import CutsomPagination
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser

"""
class ProductViewSet(viewsets.ViewSet):
    permission_classes = []
    pagination_class = CutsomPagination
    queryset = Product.objects.all()

    def list(self, request):
        ser_data = ProductSerializer(instance=self.queryset, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        ser_data = ProductSerializer(instance=product)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        ser_data = ProductSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        ser_data = ProductSerializer(instance=product, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destory(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        product.available = False
        return Response({'message': 'your product is not available'})
        
        """

class ProductViewSet(viewsets.ModelViewSet):
    pagination_class = CutsomPagination
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

"""
    def get_serializer(self, request):
        if self.action in ['list', 'retrieve']:
            return ProductViewSerializer
        else:
            return ProductSerializer
            """
