from common.pagination import CustomPagination
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductCartSerializer, EditProductCartSerializer
from .models import Cart, ProductCart



class OrderViewSet(viewsets.ModelViewSet):
    """
    using this class for create, display, update and delete orders

    Args:
        arg1:int
                id = user enter a number for id
        arg2:int
                cart = user enter a number for cart
        arg3:int
                product = user enter a number for product
        arg4:int
                quantity = user enter a number for quantity
        -----------------------------
        for update you can only send a number for quantity

    Returns:
        -----------------------
        this return some data that include details of order
    """
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    queryset = ProductCart.objects.select_related(
        'cart__user').select_related('product')
    http_method_names = ['post', 'get', 'patch', 'delete']

    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(cart__user=self.request.user)
      
    def get_serializer_class(self):
        if self.action == 'partial_update':
            return EditProductCartSerializer
        return ProductCartSerializer  
    
    def perform_create(self, serializer):
        user = self.request.user
        cart = Cart.objects.get_or_create(user=user, enable=True)
        serializer.validated_data.update(cart=cart[0])
        super().perform_create(serializer) # associated to logs
