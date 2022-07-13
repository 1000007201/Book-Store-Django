from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializers import AddBookSerializer, GetBookSerializer, GetBookPageSerializer
from .models import Book
from .validate import add_book_validator, check_superuser
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from common.jwt_token import token_required

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class AddBookApiView(GenericAPIView):
    serializer_class = AddBookSerializer
    permission_classes = ()
    authentication_classes = ()

    @method_decorator(token_required)
    def post(self, request, user_id):
        # user_id = token_decode(request)
        # if not type(user_id) == int:
        #     return Response(user_id)
        user_obj = check_superuser(user_id)
        print(type(user_obj))
        if type(user_obj) == dict:
            return Response(user_obj)
        data = request.data
        data_dict = data.dict()
        # data_dict.pop('csrfmiddlewaretoken')
        validated_data = add_book_validator(data_dict)
        if validated_data:
            if validated_data.get('Error') == 'Book already exist':
                book = Book.objects.get(name=data.get('name'))
                book.quantity += int(data.get('quantity'))
                book.save()
                return Response({'Message': 'Book already exist so quantity updated', 'Code': 200})
            return Response(validated_data)
        book = Book.objects.create(**data_dict, total_book_added=data_dict.get('quantity'))
        book.save()
        return Response({'Message': 'Book added', 'Code': 200})


class GetBookApiView(GenericAPIView):
    authentication_classes = ()
    serializer_class = GetBookSerializer

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, id=None):
        if id:
            book = Book.objects.get(pk=id)
            serializer = GetBookSerializer(book)
            return Response({'Data': serializer.data, 'Code': 200})
        book = Book.objects.order_by('-rating').all()
        domain = get_current_site(request).domain
        abs_url = reverse('get_book')
        surl = 'http://'+domain+abs_url
        print(surl)
        page_no = request.query_params.get('page')
        paginator = Paginator(book, 12)
        page_obj = paginator.get_page(page_no)
        serializer = GetBookPageSerializer(page_obj, many=True)
        data = {}
        if page_obj.has_next():
            next_page_url = f'{surl}?page={page_obj.next_page_number()}'
            data['next_page'] = next_page_url
        if page_obj.has_previous():
            prev_page_url = f'{surl}?page={page_obj.previous_page_number()}'
            data['prev_page'] = prev_page_url
        data['Data'] = serializer.data
        data['code'] = 200
        print('DATA')
        return Response(data)

    @method_decorator(token_required)
    def delete(self, request, user_id, id):
        # user_id = token_decode(request)
        # if not type(user_id) == int:
        #     return Response(user_id)
        user_obj = check_superuser(user_id)
        print(type(user_obj))
        if type(user_obj) == dict:
            return Response(user_obj)
        book = Book.objects.get(pk=id)
        book.quantity = 0
        book.total_book_added = 0
        book.save()
        return Response({'Message': 'Book Deleted', 'Code': 200})

    @method_decorator(token_required)
    def patch(self, request, user_id, id):
        # user_id = token_decode(request)
        # if not type(user_id) == int:
        #     return Response(user_id)
        user_obj = check_superuser(user_id)
        print(type(user_obj))
        if type(user_obj) == dict:
            return Response(user_obj)
        book = Book.objects.get(pk=id)
        data = request.data
        serializer = GetBookSerializer(instance=book, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Message': 'Book updated', 'Code': 200})
