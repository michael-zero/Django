from django.views.generic import TemplateView


# Puxar do BD
from .models import Servico, Funcionario

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Recupera o contexto
        context = super(IndexView, self).get_context_data(**kwargs)
        # captura todos por qualquer ordem 
        context['servicos'] = Servico.objects.order_by('?').all() 
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context


class TesteView(TemplateView):
    template_name = '404.html'