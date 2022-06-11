from django.db import models
choices = [
    (0, 'zero'),
    (1, 'one'),
    (2, 'two'),
    (3, 'three'),
    (4, 'four'),
    (5, 'five')
]


class Book(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    author = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)
    image_field = models.FileField(upload_to='images/', max_length=250, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=400)
    date_updated = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(choices=choices, blank=False)
    total_book_added = models.IntegerField()

    def __str__(self):
        return self.name
