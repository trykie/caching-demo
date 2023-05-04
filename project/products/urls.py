from django.urls import path
from .views import cached_product_list_view, product_list_view

urlpatterns = [
    path('', product_list_view),
    path('cache/', cached_product_list_view),
]
