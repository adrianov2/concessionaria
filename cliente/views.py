from django.shortcuts import render
from django.views.generic import CreateView
from .models import Cliente

# Create your views here.

class ClienteCreateView(CreateView):
     model = Cliente
     template_name = 'cadastrar/cliente.html'

     fields = '__all__'


# Create your views here.
