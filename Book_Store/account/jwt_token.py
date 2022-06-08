from rest_framework_simplejwt.tokens import RefreshToken
from jwt import decode
from django.conf import settings
from .utils import Utils


def get_token(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }


def get_user(request):
    # token = request.headers.get('Authorization')
    short_token = request.headers.get('Token')
    if not short_token:
        short_token = request.query_params.get('token')
    # data = decode(token.split()[1], settings.SECRET_KEY, 'HS256')
    token = Utils.true_token(short_token)
    data = decode(token, settings.SECRET_KEY, 'HS256')
    user_id = data['user_id']
    return user_id


