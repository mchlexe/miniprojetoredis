from rest_framework import serializers
from .models import Produto, Item


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id',
                  'nome',
                  'preco',
                  'estoque')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id',
                  'pedido_id',
                  'produto_id',
                  'quantidade')