from rest_framework_simplejwt.tokens import RefreshToken
from jwt import decode
from django.conf import settings
from .utils import Utils
from .custom_exceptions import TokenRequired


def get_token(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }


def token_decode(request):
    try:
        # token = request.headers.get('Authorization')
        short_token = request.headers.get('Token')
        if not short_token:
            short_token = request.query_params.get('token')
        if not short_token:
            raise TokenRequired('Token Required', 404)
        index = short_token.find('.')
        # data = decode(token.split()[1], settings.SECRET_KEY, 'HS256')
        if index == -1:
            token = Utils.true_token(short_token)
        else:
            token = short_token
        print(token)
        data = decode(token, settings.SECRET_KEY, 'HS256')
        user_id = data['user_id']
        return user_id
    except TokenRequired as exception:
        return exception.__dict__
    except Exception as e:
        return {'Error': str(e), 'Code': 404}
