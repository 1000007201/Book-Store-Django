from .models import Book
from django.contrib.auth import get_user_model
from .custom_exception import NullField, BookAlreadyExist, NotSuperUser

User = get_user_model()


def add_book_validator(data):
    name = data.get('name')
    author = data.get('author')
    price = data.get('price')
    quantity = data.get('quantity')
    try:
        book = Book.objects.filter(name=name).first()
        if not name or not author or not price or not quantity:
            # if not any([name, ])
            raise NullField('You have to enter all values', 404)
        if book:
            raise BookAlreadyExist('Book already exist', 404)
    except NullField as exception:
        return exception.__dict__
    except BookAlreadyExist as exception:
        return exception.__dict__


def check_superuser(user_id):
    try:
        user = User.objects.get(pk=user_id)
        if not user.is_superuser:
            raise NotSuperUser('Only Admin is allowed', 404)
        return user
    except NotSuperUser as exception:
        return exception.__dict__
    except Exception as e:
        return dict({'Error': str(e), 'Code': 404})



