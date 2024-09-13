from celery import shared_task
from django.core.mail import send_mail
from .models import StockMonitor, Record
from my_dashboard.trade_api.b3_api import get_last_records
from datetime import datetime
from celery import shared_task
from .models import StockMonitor, Record
from .trade_api import get_last_records  # Supondo que você tenha essa função

@shared_task
def wake_up_monitor(symbol):
    try:
        monitor = StockMonitor.objects.get(symbol=symbol)
        # Obtenha os dados mais recentes
        data = get_last_records(symbol)
        latest_value = data['Close'].iloc[-1]

        if latest_value > monitor.supLimit or latest_value < monitor.botLimit:
            # Enviar email
            send_email_to_user(monitor.profile.user.email, symbol, latest_value)

        # Registrar o valor
        Record.objects.create(
            stockMonitor=monitor,
            stockValue=latest_value
        )

    except StockMonitor.DoesNotExist:
        pass  # O monitor pode ter sido excluído

def send_email_to_user(email, symbol, value):
    from django.core.mail import send_mail
    send_mail(
        subject=f'Alert for {symbol}',
        message=f'The stock value for {symbol} has reached {value}.',
        from_email='tta_app@mail.com',
        recipient_list=[email]
    )
