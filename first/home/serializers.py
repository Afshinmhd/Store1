from rest_framework import serializers
from .models import Product, Comment


class ProductSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ('available', 'created', 'updated')

    def get_comments(self, obj):
        result = obj.cproduct.all()
        return CommentSerializer(instance=result, many=True).data

class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'image', 'description')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'body', 'created')