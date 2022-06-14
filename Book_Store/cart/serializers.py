from rest_framework import serializers


class AddToCartSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class GetCartSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    book_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    total_price = serializers.IntegerField()


class UpdateCartSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()

