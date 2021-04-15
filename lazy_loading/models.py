from django.db import models


class Produto(models.Model):
    cod = models.IntegerField()
    descricao = models.CharField(max_length=100)
    preco = models.FloatField()
    estoque = models.IntegerField()
