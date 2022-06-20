from django.contrib.auth.models import User
from common.custom_exception import UserNotExist, BookNotExist, CartNotExist
from book.models import Book
from .models import Cart


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


def cart_authenticate(cart_id, quantity, user_id):
    cart = Cart.objects.get(pk=cart_id)
    if cart.user.id != user_id:
        raise UserNotExist('You are not authorised to make changes', 404)
    if not cart:
        raise CartNotExist('Cart not Exist', 404)
    if cart.book.quantity < quantity:
        raise BookNotExist('That much books are not available', '404')
    return cart
