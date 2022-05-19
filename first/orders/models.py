from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from home.models import Product


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
        related_name='usertocart')
    productcart = models.ManyToManyField(Product, through='ProductCart')
    enable = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.user}'


class ProductCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartrelations')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productrelations')
    quantity = models.IntegerField()
    
    def __str__(self):
        return f'{self.cart}'  