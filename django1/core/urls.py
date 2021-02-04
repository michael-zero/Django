from django.urls import path 
from .views import index, contato, current_datetime,produto

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('data', current_datetime, name='tempo'),
    path('produto/<int:id>', produto, name='produto'),
]