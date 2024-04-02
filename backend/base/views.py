from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getProducts(request):
    return Response('Hello')

@api_view(['GET'])
def getProduct(request, pk):
    product = None
    return Response('Hello')