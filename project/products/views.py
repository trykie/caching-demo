from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product


@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    results = [product.to_json() for product in products]
    return Response(results, status=status.HTTP_200_OK)
