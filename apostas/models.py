from django.db import models

# Create your models here.
class Aposta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='apostas')
    pontos = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    palpite = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    multiplicador = models.DecimalField(default=1, max_digits=3, decimal_places=2)

class Jogo(models.Model):
    status = models.CharField(max_length=100)
    idTimeA = models.IntegerField
    idTimeB = models.IntegerField
    apostadoresTimeA = models.IntegerField
    apostadoresTimeB = models.IntegerField
    timeVencedor = models.IntegerField
    golsTimeA = models.IntegerField
    golsTimeB = models.IntegerField

class Time(models.Model):
    nome = models.CharField(max_length=100)
    vitorias = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)
    empates = models.IntegerField(default=0)

class Usuario(models.Model):
    isAdmin = models.BooleanField(default=False)
    statusAtivo = models.BooleanField(default=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField
    cpf = models.CharField(max_length=100)
    dataNascimento = models.DateField
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    pontos = models.DecimalField(default=1000)
    pontos_maximo = models.DecimalField(default=1000)
    totalAcertos = models.IntegerField(default=0)