from django.contrib import admin
from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','estoque')


class InfoCliente(admin.ModelAdmin):
    list_display = ('nome', 'email')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, InfoCliente)
