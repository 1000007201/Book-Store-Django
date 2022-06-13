from rest_framework.views import APIView, Response
from cart.models import Cart
from .models import Order
from .serializers import CheckoutSerializer
from .jwt_token import token_decode
from django.contrib.auth.models import User
from .custom_exception import UserNotExist


class CheckoutApiView(APIView):
    authentication_classes = ()

    def post(self, request, cart_id):
        try:
            user_id = token_decode(request)
            if not type(user_id) == int:
                return Response(user_id)
            user = User.objects.get(pk=user_id)
            cart = Cart.objects.get(pk=cart_id)
            data = request.data
            serializer = CheckoutSerializer(data)
            address = serializer.data.get('address')
            order = Order.objects.create(user=user, book=cart.book, address=address,
                                         quantity=cart.quantity, total_price=cart.total_price)
            order.save()
            cart.delete()
            return Response({'Message': f'order placed and will be delivered at {order.address} soon', 'Code': 200})
        except UserNotExist as exception:
            return Response(exception.__dict__)
        except Exception as e:
            return Response({'Error': str(e), 'Code': 404})





