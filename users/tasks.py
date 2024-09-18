from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime
from users.models import StockMonitor, Record, Profile
from my_dashboard.trade_api.b3_api import get_last_records,get_current_price
from django.contrib.auth.models import User

@shared_task
def wake_up_monitor_task(symbol, profile_id):
    try:
        # Obter Profile e monitor
        profile = Profile.objects.get(id=profile_id)
        period = profile.monitoring_period
        monitor = StockMonitor.objects.get(symbol=symbol, profile=profile)
        # Obter último valor da ação com função definida.
        symbol_yf = symbol + '.SA'
        [latest_value,latest_data] = get_current_price(symbol_yf, num_records= 30, minutes_interval=period)
        # Verificar Tunel.
        print(f'{symbol} ::: {monitor.supLimit} , {monitor.botLimit} ')
        alertFlag = False
        if latest_value > monitor.supLimit: # Recomendação de venda
            # Enviar email
            send_email_to_user(profile.user.email, symbol, latest_value, monitor.supLimit, False)
            alertFlag = True

        elif latest_value < monitor.botLimit: # Recomendação de compra
            # Enviar email
            send_email_to_user(profile.user.email, symbol, latest_value, monitor.botLimit, True)
            alertFlag = True

        # Registrar o valor
        Record.objects.create(
            stockMonitor=monitor,
            stockValue=latest_value,
            date=latest_data,
            alert=alertFlag
        )
        
    except StockMonitor.DoesNotExist:
        print(f"Nenhum monitor encontrado para o símbolo {symbol} e perfil com ID {profile_id}.")
    except Profile.DoesNotExist:
        print(f"Perfil com ID {profile_id} não encontrado.")
    except User.DoesNotExist:
        print(f"Usuário associado ao perfil com ID {profile_id} não encontrado.")


def send_email_to_user(email, symbol, value, compare_value, buy):
    msg = f'The stock value for {symbol} has reached {value}.\n'
    if buy:
        msg += f' You should buy this stock now, as it is below your bottom Limit: {compare_value}.'
    else:
        msg += f' You should sell this stock now, as it is above your Upper Limit: {compare_value}.'
    send_mail(
        f'Alert for {symbol}',
        f'The stock value for {symbol} has reached {value}.',
        'JpAJ234@gmail.com',
        [email],
    )
