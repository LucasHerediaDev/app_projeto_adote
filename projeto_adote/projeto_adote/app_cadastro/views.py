from django.shortcuts import render
from .models import Usuario

#request = Parametro do django que permite acessar os dados que estão dentro da página
def cadastro(request):
    return render(request,'usuarios/cadastro.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.celular = request.POST.get('celular')
    novo_usuario.save()
    usuarios = {
        'usuarios': Usuario.objects.all()
    } 
    return render(request, 'usuarios/usuarios.html',usuarios)