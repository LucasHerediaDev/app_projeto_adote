from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=15)  # Certifique-se de que "max_length" está em minúsculas aqui
    email = models.EmailField(max_length=254)