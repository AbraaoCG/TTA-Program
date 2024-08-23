from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
from . import views

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
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse('Email ou senha inválido!')


    #return render(request, 'login.html')
def register(request):
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
        profile.stocks_check_period = 5  # Por exemplo, definir um período de verificação padrão
        profile.save()
        return redirect('login')
        return HttpResponse("Usuário criado com sucesso!")