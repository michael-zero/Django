from django.urls import path 
from .views import CampoCreate, AtividadeCreate
from .views import CampoUpdate, AtividadeUpdate

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastros-campo'),
    path('cadastrar/atividade/',AtividadeCreate.as_view(), name='cadastrar-atividade'),
    # EDITAR
    path('editar/campo/<int:pk>/',CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/',AtividadeUpdate.as_view(), name='editar-atividade'),
]
