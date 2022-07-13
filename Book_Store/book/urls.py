from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AddBookApiView, GetBookApiView

urlpatterns = [
    path('add/', AddBookApiView.as_view()),
    path('get/<str:id>', GetBookApiView.as_view()),
    path('get/', GetBookApiView.as_view(), name='get_book')
]


