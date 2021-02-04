from django.db import models

#definição de um modelo
class Produto(models.Model):
    nome = models.CharField('Nome', max_length = 35)
    preco = models.DecimalField('Preço', decimal_places=2,max_digits=8)
    estoque = models.IntegerField('Estoque')

    #forma como o obj será apresentado
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length = 100)
    sobrenome = models.CharField('sobrenome', max_length = 100)
    email = models.EmailField('E-mail', max_length = 40)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
