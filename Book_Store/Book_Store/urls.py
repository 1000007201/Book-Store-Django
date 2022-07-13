from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from Book_Store import settings

schema_view = get_swagger_view(title='Book-Store API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls')),
    path('api/book/', include('book.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/order/', include('order.urls')),
    path('swagger/', schema_view)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
