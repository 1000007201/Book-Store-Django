from rest_framework.views import APIView, Response
from .serializers import AddToCartSerializer, UpdateCartSerializer
from .jwt_token import token_decode
from .validate import user_authenticate, book_authenticate, cart_authenticate
from .models import Cart
from .custom_exception import BookNotExist, UserNotExist, CartNotExist


class AddToCartAPIView(APIView):
    authentication_classes = ()

    def get(self, request):
        try:
            user_id = token_decode(request)
            if not type(user_id) == int:
                return Response(user_id)
            user = user_authenticate(user_id)
            cart = Cart.objects.filter(user=user)
            serializer = AddToCartSerializer(instance=cart, many=True)
            return Response({'Data': serializer.data, 'Code': 200})
        except UserNotExist as exception:
            return Response(exception.__dict__)
        except Exception as e:
            return Response({'Error': str(e), 'Code': 404})

    def post(self, request):
        try:
            user_id = token_decode(request)
            if not type(user_id) == int:
                return Response(user_id)
            data = request.data
            serializer = AddToCartSerializer(data)
            data_dict = dict(serializer.data)
            book_id = data_dict.get('book_id')
            quantity = data_dict.get('quantity')
            user = user_authenticate(user_id)
            book = book_authenticate(book_id, quantity)
            cart = Cart.objects.create(user=user, book=book, quantity=quantity)
            cart.save()
            return Response({'Message': f'{book.name} added to cart', 'Code': 200})
        except BookNotExist as exception:
            return Response(exception.__dict__)
        except UserNotExist as exception:
            return Response(exception.__dict__)
        except Exception as e:
            return Response({'Error': str(e), 'Code': 404})


class UpdateCartApiView(APIView):
    authentication_classes = ()

    def patch(self, request, cart_id):
        try:
            user_id = token_decode(request)
            if not type(user_id) == int:
                return Response(user_id)
            data = request.data
            serializer = UpdateCartSerializer(data)
            quantity = serializer.data.get('quantity')
            cart = cart_authenticate(cart_id, quantity, user_id)
            cart.quantity = quantity
            cart.save()
            return Response({'Message': 'Cart updated', 'Code': 200})
        except CartNotExist as exception:
            return Response(exception.__dict__)
        except UserNotExist as exception:
            return Response(exception.__dict__)
        except Exception as e:
            return Response({'Error': str(e), 'Code': 404})

    def delete(self, request, cart_id):
        try:
            user_id = token_decode(request)
            if not type(user_id) == int:
                return Response(user_id)
            cart = Cart.objects.get(pk=cart_id)
            if cart.user.id != user_id:
                raise UserNotExist('You are not authorised user to make changes', 404)
            cart.delete()
            return Response({'Message': 'Cart Deleted', 'Code': 200})
        except UserNotExist as exception:
            return Response(exception.__dict__)
        except Exception as e:
            return Response({'Error': str(e), 'Code': 404})

