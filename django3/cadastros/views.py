from django.views.generic.edit import CreateView, UpdateView
from .models import Atividade, Campo
from django.urls import reverse_lazy

class CampoCreate(CreateView):
    model = Campo
    # lista campos que aparecerão no form 
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    # Depois que cadastrar com sucesso, redireciona pro index 
    success_url = reverse_lazy('index')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero','descricao','pontos','detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


# UPDATE

class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero','descricao', 'pontos','detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')