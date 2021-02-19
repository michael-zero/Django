from django.db import models

class Campo(models.Model):
    nome = models.CharField(max_length=50, help_text='Digite um nome fácil')
    descricao = models.CharField(max_length=150, verbose_name='Descrição')

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name='Número', unique=True)
    descricao = models.CharField(verbose_name='Descrição', max_length=150)
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=100, blank=True, null=True)

    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {} ({})".format(self.numero, self.descricao, self.campo.nome)