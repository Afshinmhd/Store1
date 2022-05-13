from django.contrib import admin
from .models import Category, Product, Comment
admin.site.register(Category)
admin.site.register(Comment)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)
