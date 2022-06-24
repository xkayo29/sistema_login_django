from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.


def home(request):
    return render(request, 'home.html')


# formulário de cadastro de usuários
def create(request):
    return render(request, 'create.html')


# Inserindo dados dos usuários no banco
def store(request):
    data = {}
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'Foram digitadas senhas diferentes, tente novamente!'
        data['class'] = 'alert-danger'

    if request.POST['name'] and request.POST['user'] and request.POST['password'] \
            and request.POST['password-conf'] \
            and request.POST['email'] is not None:
        user = User.objects.create_user(request.POST['name'], request.POST['email'],
                                        request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    else:
        data['msg'] = 'Você precisa preencher todos os campos!'
    return render(request, 'create.html', data)


# Formulário do painel de login
def painel(request):
    return render(request, 'painel.html')


# Processamento de login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)


# Página inicial do sistema
def dashboard(request):
    return render(request, 'dashboard/home.html')
