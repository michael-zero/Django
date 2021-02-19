from django.views.generic.edit import CreateView
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