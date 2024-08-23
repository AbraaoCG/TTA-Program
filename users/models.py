from django.contrib.auth.models import User
from django.db import models
import json
import pandas as pd

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stocks_check_period = models.PositiveIntegerField(default=5)  # em minutos
    monitored_stocks = models.JSONField(default=list)  # Para armazenar a lista de dicionários

    def save(self, *args, **kwargs):
        # Serializar DataFrames para JSON antes de salvar
        for stock in self.monitored_stocks:
            if 'dataframe' in stock:
                stock['dataframe'] = stock['dataframe'].to_json()
        super().save(*args, **kwargs)

    def load_dataframes(self):
        # Desserializar DataFrames após carregar
        for stock in self.monitored_stocks:
            if 'dataframe' in stock:
                stock['dataframe'] = pd.read_json(stock['dataframe'])
