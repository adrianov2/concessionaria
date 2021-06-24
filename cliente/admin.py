from django.contrib import admin

from .models import Cliente, Reservar, Pontos_de_avaliacao, Marca, Cor, Entrega, Modo_pagamento, Depoimento


admin.site.register(Cliente)
admin.site.register(Reservar)
admin.site.register(Pontos_de_avaliacao)
admin.site.register(Marca)
admin.site.register(Cor)
admin.site.register(Entrega)
admin.site.register(Modo_pagamento)
admin.site.register(Depoimento)

# Register your models here.


