from rest_framework import serializers
from .models import Cart
from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'image_field', 'price']


class AddToCartSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class GetCartSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    book = BookSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'book', 'quantity']


class UpdateCartSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()

