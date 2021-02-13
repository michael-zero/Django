from django.views.generic import FormView, TemplateView
# Retira o template view, pois tem o form na pagina
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages
# Puxar do BD
from .models import Servico, Funcionario

# página que contem um formulário
class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        # Recupera o contexto
        context = super(IndexView, self).get_context_data(**kwargs)
        # captura todos por qualquer ordem 
        context['servicos'] = Servico.objects.order_by('?').all() 
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context

# form valido, manda pro index
    def form_valid(self, form, *args, **kwargs):
        # envia email
        form.send_mail()
        # msg de sucesso
        messages.success(self.request,'E-mail enviado com sucesso')
        # retorna pra index
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args,**kwargs):
        messages.error(self.request,'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form,*args,**kwargs)

class TesteView(TemplateView):
    template_name = '404.html'