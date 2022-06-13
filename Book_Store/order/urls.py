from django.urls import path
from .views import CheckoutApiView

urlpatterns = [
    path('checkout/<int:cart_id>', CheckoutApiView.as_view())
]
