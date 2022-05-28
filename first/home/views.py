from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductViewSerializer
from .models import Product
from common.pagination import CustomPagination
from .permissions import IsOwnOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    """
    using this class for create, update, display and delete products
    

    Args:
    ------------------------------------------
        arg1:int 
                category = user enter a number for category
        arg2:str 
                name = user enter a name
        arg3:str 
                slug = user enter a slug
        arg4:float 
                category = user enter a price
        arg5: 
                image = user upload an image.it can be null
        arg6:str
                description = user enter some description
    Return:
    --------------------------------------
    this return a list of property of products
    """
    permission_classes = [IsOwnOrReadOnly]
    pagination_class = CustomPagination
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
