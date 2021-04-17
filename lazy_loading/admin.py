from django.contrib import admin
from .models import Produto,Cliente,Item,Pedido

class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'estoque')
    list_display_links = ('id', 'nome')
    search_fields = ('cod',)
    # list_filter = ('nome',)
    list_per_page = 20

admin.site.register(Produto, ListandoProdutos)
admin.site.register(Cliente)
admin.site.register(Item)
admin.site.register(Pedido)