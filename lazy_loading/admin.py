from django.contrib import admin
from .models import Produto

class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'estoque')
    list_display_links = ('id', 'nome')
    search_fields = ('cod',)
    # list_filter = ('nome',)
    list_per_page = 20

admin.site.register(Produto, ListandoProdutos)