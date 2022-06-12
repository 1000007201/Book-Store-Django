from django.contrib import admin
from django.urls import path, include
from .views import AddToCartAPIView

urlpatterns = [
    path('add/cart/', AddToCartAPIView.as_view())
]