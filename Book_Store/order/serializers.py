from rest_framework import serializers


class CheckoutSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=300)

