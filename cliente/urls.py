from django.contrib import admin
from django.urls import path
from .views import ClienteCreateView

urlpatterns = [
    path('cadastra/cliente', ClienteCreateView.as_view(), name="cadastra_cliente"),
]