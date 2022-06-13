from rest_framework import serializers


class AddToCartSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    book_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class UpdateCartSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()

