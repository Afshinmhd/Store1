from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from home.models import Product


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='user',   
                            related_name='users')
    paid = models.BooleanField(_('paid'), default=False)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        ordering = ('paid', '-updated')

    def __str__(self):
        return f'{self.user}'

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='order',
                            related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')
    quantity = models.IntegerField(_('quantity'), default=1)
    price = models.IntegerField(_('price'))

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.quantity * self.price