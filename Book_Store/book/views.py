from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializers import AddBookSerializer
from .models import Book
from .validate import add_book_validator
from rest_framework.response import Response


class AddBookApiView(GenericAPIView):
    serializer_class = AddBookSerializer
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        data = request.data
        print(type(data.get('price')))
        validated_data = add_book_validator(data)
        print(validated_data)
        if validated_data:
            if validated_data.get('Error') == 'Book already exist':
                book = Book.objects.get(name=data.get('name'))
                book.quantity += int(data.get('quantity'))
                book.save()
                return Response({'Message': 'Book already exist so quantity updated', 'Code': 200})
            return Response(validated_data)
        book = Book.objects.create(name=data.get('name'),
                                   author=data.get('author'), quantity=data.get('quantity'), price=data.get('price'),
                                   image_field=data.get('image_field'))
        book.save()
        return Response({'Message': 'Book added', 'Code': 200})

