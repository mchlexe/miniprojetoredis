from djongo import models
from django.urls import reverse
from django.core.cache import cache

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    estoque = models.IntegerField(default=0)

    def get_absolute_url(self):
        cache.clear()
        return reverse('produtos')

    def __str__(self):
        return str(self.id) + ' - ' + self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)

    def get_absolute_url(self):
        cache.clear()
        return reverse('clientes')

    def __str__(self):
        return str(self.id) + ' - ' + self.nome


class Pedido(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total = models.FloatField(default=0, editable=False)

    def __str__(self):
        cache.clear()
        return str(self.id) + ' - ' + self.cliente.nome + ' - Total: ' + str(self.total)

    def get_absolute_url(self):
        return reverse('pedidos')

class Item(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        cache.clear()
        return str(self.produto.nome) + ' - Quantidade: ' + str(self.quantidade)

    def get_absolute_url(self):
        return reverse('pedidos')