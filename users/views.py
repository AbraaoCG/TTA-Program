from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import LogoutView
from .models import Profile
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def login_user(request):
    # Caso o método seja GET, renderiza o template login.html
    if request.method == "GET": 
        return render(request, 'login.html')
    else: # Caso contrário (POST), realizar login mediante autenticação.
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password=password)
        if user:
            login(request = request, user = user)
            user_id = request.user.id
            request.session['user_id'] = request.user.id
            return redirect('dashboard')
        else:
            return HttpResponse('Email ou senha inválido!')


    #return render(request, 'login.html')
def register_user(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user = User.objects.filter(username = username).first()
        if user:
            return HttpResponse('Já existe um usuário com esse Email!')
        
        user = User.objects.create_user(username, email, password)
        user.save()

        # Cria e inicializa o perfil do usuário
        profile = Profile.objects.create(user=user)
        profile.monitoring_period = 5  # Por exemplo, definir um período de verificação padrão
        profile.save()
        return redirect('login')

def logout_user(request):
    # Reseta a sessão
    request.session.flush()  
    # Faz logout do usuário
    logout(request)
    return redirect('login')


@csrf_exempt
def update_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('value')
        request.user.email = email
        request.user.save()
        return JsonResponse({'success': True})

@csrf_exempt
def update_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        password = data.get('value')
        username = request.user.username
        request.user.set_password(password)
        request.user.save()
        user = authenticate(username = username, password=password)
        if user:
            login(request = request, user = user)
        else:
            return redirect('login')
        return JsonResponse({'success': True})

@csrf_exempt
def update_monitoring_period(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        monitoring_period = data.get('value')
        profile = Profile.objects.get(user=request.user)
        profile.monitoring_period = monitoring_period
        profile.save()
        return JsonResponse({'success': True})