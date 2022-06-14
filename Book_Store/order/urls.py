from django.urls import path
from .views import CheckoutApiView, GetOrderAPIView

urlpatterns = [
    path('checkout/<int:cart_id>', CheckoutApiView.as_view()),
    path('get/', GetOrderAPIView.as_view())
]
