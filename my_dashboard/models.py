from django.db import models
import datetime
class Acao(models.Model):
    nome = models.CharField(max_length=55)
    sigla = models.CharField(max_length=5)
    ultimoValor = models.FloatField()
    dataUltimoValor = models.DateTimeField(default = datetime.datetime.now)
    limSuperior = models.FloatField()
    limInferior = models.FloatField()

    def __str__(self) -> str:
        return self.ultimoValor
