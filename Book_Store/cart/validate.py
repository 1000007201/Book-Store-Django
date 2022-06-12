from django.contrib.auth.models import User
from .custom_exception import UserNotExist, BookNotExist
from book.models import Book


def user_authenticate(user_id):
    user = User.objects.get(pk=user_id)
    if not user:
        raise UserNotExist('User not Exist', 404)
    return user


def book_authenticate(book_id, quantity):
    book = Book.objects.get(pk=book_id)
    if not book:
        raise BookNotExist('Book not Exist', 404)
    if quantity > book.quantity:
        raise BookNotExist('That much books are not available', 404)
    return book