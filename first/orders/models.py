from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from home.models import Product


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                            verbose_name='user', related_name='usertocart')
    productcart = models.ManyToManyField(Product, verbose_name='productcart', 
                                        through='ProductCart')
    enable = models.BooleanField(_('enable'), default=True)
    
    def __str__(self):
        return f'{self.user}'


class ProductCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='cart',
                            related_name='cartrelations')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product',
                                related_name='productrelations')
    quantity = models.IntegerField(_('quantity'))
    
    def __str__(self):
        return f'{self.cart}'  