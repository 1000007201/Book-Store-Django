from rest_framework import serializers
from .models import Book


class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'name',
            'author',
            'price',
            'quantity',
            'image_field',
            'description',
            'rating'
        ]
        required_field = ['name', 'author', 'price', 'quantity', 'rating']


class GetBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'image_field','name', 'author', 'price', 'quantity', 'description', 'rating']


class GetBookPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'image_field', 'name', 'price', 'rating', 'author', 'quantity']