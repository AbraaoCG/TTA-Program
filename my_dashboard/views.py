from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StockSymbol  # Importe seu modelo de símbolo de ações
from users.models import Profile, StockMonitor  # Importe seu modelo de perfil e monitor de ações

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

import pandas as pd

from my_dashboard.trade_api.b3_api import get_last_records
import json

@login_required(login_url='/auth/login/')
def dashboard(request):
    profile = request.user.profile # Obter profile do usuário logado
    stock_monitors = StockMonitor.objects.filter(profile=profile) # Obter lista de monitores do usuário logado

    return render(request, 'home.html', {'profile': profile , 'stock_monitors': stock_monitors})


def dashB_redirect(request):
    return redirect('/dashboard/')

@csrf_exempt
def suggestions_view(request):
    query = request.GET.get('query', '').strip()
    if not query:
        return JsonResponse([], safe=False)
    
    # Filtrar símbolos que começam com a consulta
    symbols = StockSymbol.objects.filter(symbol__icontains=query).values_list('symbol', flat=True)
    return JsonResponse(list(symbols), safe=False)


def get_stock_data(request):
    if request.method == 'GET':
        ticker = request.GET.get('ticker')
        request.session['selected_ticker'] = ticker
        profile = Profile.objects.get(user=request.user)
        period = profile.monitoring_period
        if ticker:
            data = get_last_records(ticker, num_records= 30, minutes_interval=period)  # Exemplo com 10 registros e intervalo de 15 minutos
            
            # Gera o gráfico com os dados obtidos
            graph_json = getGraph(data, title=f'{ticker} Stock Price')
            
            # Retorna o gráfico como JSON
            return JsonResponse({'graph': graph_json})
        else:
            return JsonResponse({'success': False, 'error': 'Ticker not provided'})

def get_graph_view(request):
    # Verifica se há um token selecionado na sessão
    ticker = request.session.get('selected_ticker')
    
    if ticker:
        # Buscar dados da API
        data = get_last_records(ticker, num_records=30, minutes_interval=5)
    else:
        # Gráfico vazio se nenhum ticker estiver selecionado
        data = pd.DataFrame({'Date': [], 'Close': []})

    # Criar o gráfico
    graph_json = getGraph(data, title=f"Stock Price - {ticker}")

    return JsonResponse({'graph': graph_json})

# Função para criar um gráfico com os dados fornecidos . NÃO É VIEW!
def getGraph(data, title):
    if data.empty:
        fig = go.Figure()  # Gráfico vazio
    else:
        fig = px.line(data, x=data.index, y='Close', title=title)

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='rgba(0,0,0,1)',  # Preto para o texto
        title_font_size=24,            # Tamanho da fonte do título
        xaxis_title_font_size=18,      # Tamanho da fonte do título do eixo x
        yaxis_title_font_size=18,      # Tamanho da fonte do título do eixo y
        xaxis_tickfont_size=16,        # Tamanho da fonte dos rótulos do eixo x
        yaxis_tickfont_size=16,        # Tamanho da fonte dos rótulos do eixo y
        legend_font_size=14,           # Tamanho da fonte da legenda
    )
    fig.update_yaxes(showspikes=True,spikesnap="cursor")
    return pio.to_json(fig)


# Função para definir um monitor de ações
def setMonitor(request):
    if request.method == 'POST':
        # Obter dados do POST e do usuário.
        data = json.loads(request.body)
        symbol = data.get('symbol').replace('.SA', '')  # Remover '.SA' do ticker
        # Obter os limites superior e inferior, usando casting para float.  
        supLimit = float(data.get('upper'))
        botLimit = float(data.get('bottom'))
        profile = Profile.objects.get(user=request.user)
        
        # Verificar se o ticker já está sendo monitorado
        if profile.stockmonitor_set.filter(symbol=symbol).exists():
            return JsonResponse({'success': False, 'error': 'Ticker already being monitored'})
        
        # Criar um novo monitor de ações
        monitor = profile.stockmonitor_set.create(symbol=symbol, supLimit=supLimit, botLimit=botLimit)
        monitor.save()
        
        # Retornar uma resposta de sucesso
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

# Função para obter monitores de ações do usuário
def get_stock_monitors(request):
    profile = request.user.profile
    stock_monitors = profile.stockmonitor_set.all()
    
    monitors_data = [
        {'symbol': monitor.symbol, 'supLimit': monitor.supLimit, 'botLimit': monitor.botLimit}
        for monitor in stock_monitors
    ]
    
    return JsonResponse({'stock_monitors': monitors_data})


# Função para atualizar um monitor de uma ação.
def update_monitor(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        upper_limit = float(data.get('upper').replace(',', '.'))
        bottom_limit = float(data.get('bottom').replace(',', '.'))
        symbol = data.get('symbol')

        print(f'symbol : {symbol}')

        profile = Profile.objects.get(user=request.user)
        print(symbol)
        monitor = StockMonitor.objects.get(profile=profile, symbol=symbol)
        
        monitor.supLimit = upper_limit
        monitor.botLimit = bottom_limit
        monitor.save()
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



@login_required(login_url='/auth/login/')
@csrf_exempt
def delete_monitor(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        symbol = data.get('symbol')
        
        try:
            profile = Profile.objects.get(user=request.user)
            monitor = StockMonitor.objects.get(profile=profile, symbol=symbol)
            monitor.delete()
            return JsonResponse({'success': True})
        except StockMonitor.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Monitor not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})