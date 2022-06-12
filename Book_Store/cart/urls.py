from django.contrib import admin
from django.urls import path, include
from .views import AddToCartAPIView, UpdateCartApiView

urlpatterns = [
    path('add/cart/', AddToCartAPIView.as_view()),
    path('update/cart/<str:cart_id>', UpdateCartApiView.as_view())
]