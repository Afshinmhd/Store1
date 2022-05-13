from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory',
                                    verbose_name='sub_category', null=True, blank=True)
    is_sub = models.BooleanField(_('is_sub'), default=False)
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ManyToManyField(Category, verbose_name='category', related_name='products')
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    price = models.DecimalField(_('price'), max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,verbose_name='user',
                            related_name='cuser')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product',
                                related_name='cproduct')
    body = models.TextField(_('body'))
    created = models.DateTimeField(_('created'), auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user}-{self.body[:40]}'
