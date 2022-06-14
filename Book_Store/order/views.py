from rest_framework.views import APIView, Response
from cart.models import Cart
from .models import Order
from .serializers import CheckoutSerializer, GetOrderSerializer
from .jwt_token import token_required
from django.contrib.auth.models import User
from .custom_exception import UserNotExist, BookNotExist, TokenRequired
from django.utils.decorators import method_decorator


class CheckoutApiView(APIView):
    authentication_classes = ()

    @method_decorator(token_required)
    def post(self, request, user_id, cart_id):
        try:
            # user_id = token_decode(request)
            # if not type(user_id) == int:
            #     return Response(user_id)
            user = User.objects.get(pk=user_id)
            cart = Cart.objects.get(pk=cart_id)
            book = cart.book
            if book.quantity < cart.quantity:
                raise BookNotExist('That much books are not in stock', 404)
            data = request.data
            serializer = CheckoutSerializer(data)
            address = serializer.data.get('address')
            order = Order.objects.create(user=user, book=cart.book, address=address,
                                         quantity=cart.quantity, total_price=cart.total_price)
            order.save()
            book.quantity -= cart.quantity
            book.save()
            cart.delete()
            return Response({'Message': f'order placed and will be delivered at {order.address} soon', 'Code': 200})
        except UserNotExist as exception:
            return Response(exception.__dict__)
        except BookNotExist as exception:
            return Response(exception.__dict__)
        except Exception as e:
            return Response({'Error': str(e), 'Code': 404})


class GetOrderAPIView(APIView):

    def get(self, request):
        order = Order.objects.all()
        serializer = GetOrderSerializer(instance=order, many=True)
        return Response({'Data': serializer.data, 'Code': 200})

