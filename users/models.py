from django.contrib.auth.models import User
from django.db import models
import json
import pandas as pd
import datetime

class Profile(models.Model):
    # Cada user tem uma classe Profile associada. Um para um.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # A implementação define que um usuário tem um tempo fixo de verificação do valor de todas as ações, em minutos.
    monitoring_period = models.PositiveIntegerField(default=5)

class StockMonitor(models.Model):
    # Cada monitor de ação armazena nome, símbolo, último valor, data do último valor, limite superior e limite inferior.
    name = models.CharField(max_length=30)
    symbol = models.CharField(max_length=10)
    datelastValue = models.DateTimeField(default = datetime.datetime.now)
    supLimit = models.FloatField()
    botLimit = models.FloatField()
    
    # Cada user/profile tem uma lista de ações monitoradas. Cada ação é uma classe 'monitor de ações'. Um para muitos.
    # Essa "Lista" está escondida pela estrutua 'ForeignKey'

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    

class Record(models.Model):
    date = models.DateTimeField(default = datetime.datetime.now)
    stockValue = models.FloatField()
    stockMonitor = models.ForeignKey(StockMonitor, on_delete=models.CASCADE)
    # Adicione outros campos conforme necessário


