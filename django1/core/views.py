from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Produto
from django.template import loader

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def index(request):
    produtos = Produto.objects.all()
    #print(f'user: {request.user.email}')
    #print(f" Navegador: {request.headers['User-Agent']} Método: {request.method} Host: {request.headers['host']}")
  
    # if str(request.user) == 'AnonymousUser':
    #     teste = 'Usuário não logado'
    # else:
    #     teste = 'Usuário logado'
    
    context = {
        'Curso': 'Programação web com django framework',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request,id):
    #prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)
    #print(prod)
    context = {
        'produto': prod
    }
    return render(request,'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8',status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8',status=500)  