from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from .models import Produto
import datetime


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def index(request, param):

    produto = get_object_or_404(Produto, cod=param)

    dados = {
        'cod': produto.cod,
        'descricao': produto.descricao,
        'preco': produto.preco,
        'estoque': produto.estoque
    }

    html = f"<html><body>{str(dados)}</body></html>"
    return HttpResponse(html)
