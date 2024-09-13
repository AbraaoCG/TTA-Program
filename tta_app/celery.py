from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define o módulo de configuração padrão para o Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tta_app.settings')

app = Celery('tta_app')

# Usando string aqui para evitar problemas com a importação de aplicativos quando o worker é iniciado
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carregue os módulos de tarefas de todos os aplicativos Django
app.autodiscover_tasks()
