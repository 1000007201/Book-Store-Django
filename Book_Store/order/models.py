from django.db import models
from book.models import Book
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False)
    address = models.TextField(max_length=300, null=False)
    total_price = models.IntegerField(null=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.name
