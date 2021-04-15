from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework.decorators import api_view
import datetime


#CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


#@cache_page(CACHE_TTL)
def index(request, param):
    try:
        produto = Produto.objects.get(id=param)
    except Produto.DoesNotExist:
        return JsonResponse({'message': 'Produto nao encontrado'}, status=status.HTTP_404_NOT_FOUND)

    produto_serializer = ProdutoSerializer(produto)
    return JsonResponse(produto_serializer.data)

def listaProdutos(request):
    try:
        produto = Produto.objects.all()
    except Produto.DoesNotExist:
        return JsonResponse({'message': 'Produto nao encontrado'}, status=status.HTTP_404_NOT_FOUND)

    produto_serializer = ProdutoSerializer(produto, many=True)
    return JsonResponse(produto_serializer.data, safe=False)

