from .models import Book
from .custom_exception import NullField, BookAlreadyExist


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
