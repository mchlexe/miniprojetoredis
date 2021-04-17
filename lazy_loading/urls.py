from django.urls import path
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings


from .views import (
    EcommerceView,
    ProdutoListView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoDeleteView,
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
    PedidosListView,
    PedidoListView,
    PedidoCreateView,
    PedidoUpdateView,
    PedidoDeleteView,
    ItemCreateView,
)


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


urlpatterns = [
    path('', EcommerceView.as_view(), name='index'),
    #PRODUTOS
    path('produtos/', cache_page(CACHE_TTL)(ProdutoListView.as_view()), name='produtos'),
    path('produtos/create/', ProdutoCreateView.as_view(), name='produtoCreate'),
    path('produtos/<int:pk>/edit/', ProdutoUpdateView.as_view(), name='produtoEdit'),
    path('produtos/<int:pk>/delete/', ProdutoDeleteView.as_view(), name='produtoDelete'),
    #CLIENTES
    path('clientes/', cache_page(CACHE_TTL)(ClienteListView.as_view()), name='clientes'),
    path('clientes/create/', ClienteCreateView.as_view(), name='clienteCreate'),
    path('clientes/<int:pk>/edit/', ClienteUpdateView.as_view(), name='clienteEdit'),
    path('clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='clienteDelete'),
    #PEDIDOS
    path('pedidos/', cache_page(CACHE_TTL)(PedidosListView.as_view()), name='pedidos'),
    path('pedidos/create/', PedidoCreateView.as_view(), name='pedidoCreate'),
    path('pedidos/<int:pedido_id>/', cache_page(CACHE_TTL)(PedidoListView.as_view()), name='pedidoDetail'),
    path('pedidos/<int:pk>/edit/', PedidoUpdateView.as_view(), name='pedidoEdit'),
    path('pedidos/<int:pk>/delete/', PedidoDeleteView.as_view(), name='pedidoDelete'),
    path('pedidos/itemcreate/', ItemCreateView.as_view(), name='itemCreate'),

]