from django.shortcuts import render
from django.views.generic import TemplateView

# Renderiza o template modelo
class IndexView(TemplateView):
    template_name = 'modelo.html'
    
class SobreView(TemplateView):
    template_name = 'sobre.html'