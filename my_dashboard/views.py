from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StockSymbol  # Importe seu modelo de símbolo de ações
from users.models import Profile

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

import pandas as pd

from my_dashboard.trade_api.b3_api import get_last_records


@login_required(login_url='/auth/login/')
def dashboard(request):
    user_id = request.session.get('user_id')
    profile = Profile.objects.get(user_id=user_id)

    return render(request, 'home.html', {'profile': profile })


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



def setMonitor(request):
    if request.method == 'POST':
        # Obter os dados do POST
        data = request.POST
        ticker = request.session.get('selected_ticker')
        supLimit = data.get('upper')
        botLimit = data.get('bottom')
        profile = Profile.objects.get(user=request.user)
        
        # # Verificar se o ticker já está sendo monitorado
        # if profile.stockmonitor_set.filter(symbol=ticker).exists():
        #     return JsonResponse({'success': False, 'error': 'Ticker already being monitored'})
        
        # Criar um novo monitor de ações
        monitor = profile.stockmonitor_set.create(symbol=ticker, supLimit=supLimit, botLimit=botLimit)
        monitor.save()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})