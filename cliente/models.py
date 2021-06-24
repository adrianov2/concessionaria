from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=10, null=False, blank=False)
    email_cliente = models.EmailField(blank=True, null=True)
    venda_concluida = models.BooleanField(blank=False, null=False)
    numero_venda = models.IntegerField(blank=False, null=False)
    observacao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=100, decimal_places=10, null=False, blank=False)


    def __str__(self):
        return self.nome + '. R$:' + str(self.valor)


class Reservar(models.Model):
    nome = models.CharField(max_length=10, null=False, blank=False)
    email_cliente = models.EmailField(blank=True, null=True)
    data = models.DateField(auto_now_add=False, blank=True, null=False)
    hora = models.TimeField(auto_now_add=False, blank=True, null=False)
    numero_venda = models.IntegerField(blank=False, null=False)


    def __str__(self):
        return self.nome


class Pontos_de_avaliacao(models.Model):
    numero_venda = models.IntegerField(blank=False, null=False)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default=10)
    nota = models.DecimalField(max_digits=10, decimal_places=1)


class Marca(models.Model):
    volkswagen = models.BooleanField(blank=False, null=False)
    chevrolet = models.BooleanField(blank=False, null=False)
    toyota = models.BooleanField(blank=False, null=False)
    honda = models.BooleanField(blank=False, null=False)
    hyundai = models.BooleanField(blank=False, null=False)
    peugeot = models.BooleanField(blank=False, null=False)
    numero_venda = models.IntegerField(blank=False, null=False)


    def __int__(self):
        return self.numero_venda


class Cor(models.Model):
    branco = models.BooleanField(blank=False, null=False)
    preto = models.BooleanField(blank=False, null=False)
    vermelho = models.BooleanField(blank=False, null=False)
    azul = models.BooleanField(blank=False, null=False)
    amarelo = models.BooleanField(blank=False, null=False)
    verde = models.BooleanField(blank=False, null=False)


    def __int__(self):
        return self.Cor


class Entrega(models.Model):
    nome = models.CharField(max_length=10, null=False, blank=False)
    email_cliente = models.EmailField(blank=True, null=True)
    data = models.DateField(auto_now_add=True, blank=True, null=False)
    hora = models.TimeField(auto_now_add=True, blank=True, null=False)
    numero_venda = models.IntegerField(blank=False, null=False)
    cor = models.CharField(max_length=10, null=False, blank=False)


    def __str__(self):
        return self.nome


class Modo_pagamento(models.Model):
    numero_venda = models.IntegerField(blank=False, null=False)
    nome = models.CharField(max_length=10, null=False, blank=False)
    email_cliente = models.EmailField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=1)
    hora_venda = models.TimeField(auto_now_add=True, blank=True, null=False)
    data_venda = models.DateField(auto_now_add=True, blank=True, null=False)
    comprovante_da_venda = models.FileField(upload_to='comprovante_venda/')
    venda_concluida = models.BooleanField(blank=False, null=False)


    def __str__(self):
        return self.nome + '. R$: ' + str(self.valor)


class Depoimento(models.Model):
        nome = models.CharField(max_length=10, null=False, blank=False)
        email_cliente = models.EmailField(blank=True, null=True)
        numero_venda = models.IntegerField(blank=False, null=False)


# Create your models here.
