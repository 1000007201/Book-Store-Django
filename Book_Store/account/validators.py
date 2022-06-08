from .custom_exceptions import FieldError
from django.contrib.auth import authenticate


def validate_password(request, data):
    username = data.data.get('username')
    old_password = data.data.get('old_password')
    new_password = data.data.get('new_password')
    conf_new_password = data.data.get('conf_new_password')
    try:
        if not username and not old_password and new_password and conf_new_password:
            raise FieldError('You have to enter all fields', 404)
        if new_password != conf_new_password:
            raise FieldError('new Passwords are not matching', 404)
        if not authenticate(request, username=username, password=old_password):
            raise FieldError('check username and old password', 404)
    except FieldError as exception:
        return exception.__dict__
    return data


def validate_login():
    pass


def validate_register():
    pass
