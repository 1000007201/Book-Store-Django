from jwt import decode
from django.conf import settings
from .utils import Utils
from django.http.response import JsonResponse
from functools import wraps


def token_required(f):
    @wraps(f)
    def token_decode(request, *args, **kwargs):
        # token = request.headers.get('Authorization')
        short_token = request.headers.get('Token')
        if not short_token:
            short_token = request.query_params.get('token')
        if not short_token:
            # raise TokenRequired('Token is missing!', 409)
            return JsonResponse({'message': 'Token is missing!', 'code': 409})
        index = short_token.find('.')
            # data = decode(token.split()[1], settings.SECRET_KEY, 'HS256')
        if index == -1:
            token = Utils.true_token(short_token)
        else:
            token = short_token
        try:
            data = decode(token, settings.SECRET_KEY, 'HS256')
            user_id = data['user_id']
        except Exception as e:
            return JsonResponse({'Error': str(e), 'Code': 409})
        return f(request, user_id, *args, **kwargs)
    return token_decode