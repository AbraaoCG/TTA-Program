from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StockSymbol  # Importe seu modelo de símbolo de ações

@login_required(login_url='/auth/login/')
def dashboard(request):
    return render(request, 'home.html')


@csrf_exempt
def suggestions_view(request):
    query = request.GET.get('query', '').strip()
    if not query:
        return JsonResponse([], safe=False)
    
    # Filtrar símbolos que começam com a consulta
    symbols = StockSymbol.objects.filter(symbol__icontains=query).values_list('symbol', flat=True)
    return JsonResponse(list(symbols), safe=False)