from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Perfil  # Importamos o seu modelo de Perfil
from django.contrib import messages
from django.contrib.auth.views import LoginView

def cadastro(request):
    if request.method == 'POST':
        usuario_nome = request.POST.get('username')
        senha = request.POST.get('password')
        confirmacao = request.POST.get('password_confirm')
        # Se você quiser capturar o telefone no cadastro, adicione um input lá e capture aqui:
        # telefone = request.POST.get('telefone')

        if senha != confirmacao:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'usuarios/cadastro.html')

        if User.objects.filter(username=usuario_nome).exists():
            messages.error(request, 'Este usuário já existe!')
            return render(request, 'usuarios/cadastro.html')

        # 1. Cria o Usuário (Autenticação)
        novo_usuario = User.objects.create_user(username=usuario_nome, password=senha)
        
        # 2. Cria o Perfil vinculado a esse usuário (Seus campos extras)
        Perfil.objects.create(usuario=novo_usuario, pontos=0) 
        
        messages.success(request, 'Conta criada com sucesso! Agora você já pode entrar.')
        return redirect('login')
        
    return render(request, 'usuarios/cadastro.html')

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    
    def get_success_url(self):
        return '/'