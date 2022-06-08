from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'confirm_password',
            ]
        extra_kwargs = {'password': {'write_only': True}}
        required_fields = ['username', 'email', 'password', 'confirm_password']


class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password']
        required_fields = fields


class ResetPassSerializer(serializers.Serializer):
    username = serializers.CharField()
    old_password = serializers.CharField(style={'input_type': 'password'})
    new_password = serializers.CharField(style={'input_type': 'password'})
    conf_new_password = serializers.CharField(style={'input_type': 'password'})

