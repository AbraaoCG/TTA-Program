import json
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from .models import StockMonitor

@receiver(post_save, sender=StockMonitor)
def update_periodic_task(sender, instance, **kwargs):
    # Cria ou atualiza o intervalo para o monitor
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=instance.profile.monitoring_period,
        period=IntervalSchedule.MINUTES
    )

    task_name = f"wake_up_monitor_{instance.symbol}"

    # Remove a tarefa existente se existir
    PeriodicTask.objects.filter(name=task_name).delete()

    PeriodicTask.objects.create(
        interval=schedule,
        name=task_name,
        task='users.tasks.wake_up_monitor',
        args=json.dumps([instance.symbol])
    )

@receiver(post_delete, sender=StockMonitor)
def delete_periodic_task(sender, instance, **kwargs):
    task_name = f"wake_up_monitor_{instance.symbol}"
    PeriodicTask.objects.filter(name=task_name).delete()
