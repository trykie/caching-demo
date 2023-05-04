from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    results = [product.to_json() for product in products]
    return Response(results, status=status.HTTP_200_OK)


@api_view(['GET'])
def cached_product_list_view(request):
    if 'products' in cache:
        # get results from cache
        products = cache.get('products')
        return Response(products, status=status.HTTP_200_OK)

    else:
        products = Product.objects.all()
        results = [product.to_json() for product in products]
        # store data in cache
        cache.set('products', results, timeout=CACHE_TTL)
        return Response(results, status=status.HTTP_200_OK)
