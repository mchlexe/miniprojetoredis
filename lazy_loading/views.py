from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.http.response import JsonResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Produto, Cliente, Pedido, Item
from .serializers import ItemSerializer
from rest_framework.decorators import api_view
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.cache import cache

import datetime


class EcommerceView(TemplateView):
    template_name = 'index.html'


#CRUD PRODUTO
class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_crud/read.html'
    context_object_name = 'produtos_list'


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto_crud/create.html'
    fields = '__all__'


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto_crud/edit.html'
    fields = ['nome','preco','estoque']


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_crud/delete.html'
    success_url = reverse_lazy('produtos')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        cache.clear()
        return super(ProdutoDeleteView, self).delete(*args, **kwargs)


#CRUD CLIENTE
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_crud/read.html'
    context_object_name = 'clientes_list'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cliente_crud/create.html'
    fields = '__all__'


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'cliente_crud/edit.html'
    fields = ['nome', 'cpf', 'telefone']


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_crud/delete.html'
    success_url = reverse_lazy('clientes')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        cache.clear()
        return super(ClienteDeleteView, self).delete(*args, **kwargs)


#CRUD PEDIDOS
class PedidosListView(ListView):
    model = Pedido
    template_name = 'pedido_crud/read.html'
    context_object_name = 'pedidos_list'


class PedidoListView(ListView):
    model = Item
    template_name = 'pedido_crud/detail.html'

    def get_context_data(self, *args, **kwargs):
        param = self.kwargs['pedido_id']
        context = super().get_context_data(*args, **kwargs)
        context['pedido'] = Pedido.objects.all().select_related().filter(id=param)
        context['item_list'] = Item.objects.all().select_related().filter(pedido_id=param)
        return context

def atualizaTotal(param):
    pedido = Pedido.objects.all().select_related().filter(id=param)
    pk = pedido[0].id
    itens = Item.objects.all().select_related().filter(pedido_id=pk).values()
    total_pedido = 0

    for item in itens:
        preco = Produto.objects.get(id=item['produto_id']).preco
        total_pedido += item['quantidade'] * preco

    pedidoDB = Pedido.objects.get(id=pk)
    pedidoDB.total = 0
    pedidoDB.total = total_pedido
    pedidoDB.save()

class PedidoUpdateView(UpdateView):
    model = Item
    template_name = 'pedido_crud/edit.html'
    fields = ['produto','quantidade','pedido']

    def form_valid(self, form):
        response = super(PedidoUpdateView, self).form_valid(form)
        param = form.data['pedido']

        atualizaTotal(param)

        return response


class PedidoCreateView(CreateView):
    model = Pedido
    template_name = 'pedido_crud/create.html'
    fields = '__all__'


class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'pedido_crud/delete.html'
    success_url = reverse_lazy('pedidos')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        cache.clear()
        return super(PedidoDeleteView, self).delete(*args, **kwargs)


class ItemCreateView(CreateView):
    model = Item
    template_name = 'pedido_crud/create.html'
    fields = '__all__'

    def form_valid(self, form):
        response = super(ItemCreateView, self).form_valid(form)
        param = form.data['pedido']

        atualizaTotal(param)

        return response


# def index(request, param):
#     try:
#         produto = Produto.objects.get(id=param)
#     except Produto.DoesNotExist:
#         return JsonResponse({'message': 'Produto nao encontrado'}, status=status.HTTP_404_NOT_FOUND)
#
#     produto_serializer = ProdutoSerializer(produto)
#     return JsonResponse(produto_serializer.data)
#
# def listaProdutos(request):
#     try:
#         produto = Produto.objects.all()
#     except Produto.DoesNotExist:
#         return JsonResponse({'message': 'Produto nao encontrado'}, status=status.HTTP_404_NOT_FOUND)
#
#     produto_serializer = ProdutoSerializer(produto, many=True)
#     return JsonResponse(produto_serializer.data, safe=False)

