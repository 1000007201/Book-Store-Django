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
            'image_field'
        ]
        required_field = ['name', 'author', 'price', 'quantity']
