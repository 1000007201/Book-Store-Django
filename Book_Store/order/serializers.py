from rest_framework import serializers
from .models import Order


class CheckoutSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=300)


class GetOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

