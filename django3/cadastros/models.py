from django.db import models

class Campo(models.Model):
    nome = models.CharField(label='nome', max_length=50)
    descricao = models.CharField(label='descrição', max_length=150, verbose_name='Descrição')

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name='Número')
    descricao = models.CharField(verbose_name='Descrição')
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=100)

    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.nome, self.campo.nome)