from __future__ import absolute_import, unicode_literals

# Importa as tarefas para que sejam registradas automaticamente
from .celery import app as celery_app

__all__ = ('celery_app',)