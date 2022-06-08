from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    author = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)
    image_field = models.FileField(upload_to='images/', max_length=250, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
