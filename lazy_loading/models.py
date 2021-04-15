from djongo import models


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + ' - ' + self.nome