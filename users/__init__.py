from __future__ import absolute_import, unicode_literals

# Isso assegura que o app Celery seja sempre importado quando Django iniciar
from tta_app.celery import app as celery_app

__all__ = ('celery_app',)