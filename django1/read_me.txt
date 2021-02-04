#============= Criando Ambiente Virtual ========================
1. python -m venv django1  #cria ambiente virtual
2. (cmd) django1\Scripts\activate.bat #ativa o ambiente virtual
   #Agora posso instalar coisas no meu projeto
3. dactivate #sai do ambiente virtual
4. rmvirtualenv (nome) #remove o ambiente virtual
#===============================================================

pip install django

#Projeto =======================================================
django-admin startproject django1 . #inicia projeto sem criar subdiretorio(.)

#Aplicação =====================================================
django-admin startapp core
add a aplicação no installed_apps = 'core' (settings.py)

#Execução
python manage.py runserver


TEMPLATES .. DIRS: ['templates'] o diretório de templates será chamado templates


#observações
1.pip freeze > requirements.txt (salva as bib's adicionadas)  

#Views 
1. ficam nas aplicações
2. cria um arquivo urls.py e importa as configs do projeto (urls)

#Routes 
1. no (PROJETO) urls.py

#migration = gerenciar o histórico do banco de dados
python manage.py makemigrations

executar a migration:
python manage.py migrate 

#admin na aplicação
 serve p/ importar os modelos e registrar na administração 
python manage.py createsuperuser

#shell
python manage.py shell
from core.models import Produto
produto = Produto(nome = "Controle ps4", preco = 569.00,estoque = 3) #sem construtor
print(dir(Produto.objects))
help(Produto.objects.get) //mostra info do método
produto.save()
produto.delete()

#============ static files 
python manage.py collectstatic => cria a pasta staticfiles com os arquivos estáticos

#===================================
python manage.py createsuperuser