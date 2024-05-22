from django.contrib import admin
from django.urls import path
from app_cadastro import views

urlpatterns = [
    #rota view responsavel, nome de referencia
    path('', views.cadastro, name='cadastro'),
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
]
