from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Atividade, Campo
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

class CampoCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    group_required = u"Administrador" 
    login_url = reverse_lazy('login')
    model = Campo
    # lista campos que aparecerão no form 
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    # Depois que cadastrar com sucesso, redireciona pro index 
    success_url = reverse_lazy('listar-campos')

class AtividadeCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero','descricao','pontos','detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')


# UPDATE

class CampoUpdate(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeUpdate(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero','descricao', 'pontos','detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')


# DELETE
class CampoDelete(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeDelete(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')


#LISTAR
# necessita de autenticação, se n tiver, vai pra login
class CampoList(GroupRequiredMixin,LoginRequiredMixin,ListView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/campo.html'
    

class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'