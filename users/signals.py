import json
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from users.models import StockMonitor
from users.views import update_periodic_task_for_monitor

@receiver(post_save, sender=StockMonitor)
def update_periodic_task(sender, instance, **kwargs):
    update_periodic_task_for_monitor(instance)


@receiver(post_delete, sender=StockMonitor)
def delete_periodic_task(sender, instance, **kwargs):
    task_name = f"wake_up_monitor_{instance.symbol}_{instance.profile.id}"
    PeriodicTask.objects.filter(name=task_name).delete()
