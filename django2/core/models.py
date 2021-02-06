from django.db import models
from stdimage import StdImageField

# SIGNALS
#processamento antes e depois 
from django.db.models import signals
#slug 
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124,124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome) 
    #mike zero => mike-zero

signals.pre_save.connect(produto_pre_save, sender=Produto)
#antes de salva, assim q produto for enviado... executa a produto_pre_save


