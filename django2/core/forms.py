from django import forms
from django.core.mail.message import EmailMessage
#Produto
from .models import Produto
#python manage.py shell
#from django import forms
#help(CharField) - info do método
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=35)
    email = forms.EmailField(label='Email', max_length=50)
    assunto = forms.CharField(label='Assunto', max_length=25)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_mail(self):
        nome = self.cleaned_data['nome'],
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto'],
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n E-mail {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject = 'email enviado pelo sistema django2',
            body=conteudo, 
            from_email = 'contato@seudominio.com.br',
            to=['contato@seudominio.com.br'],
            headers={'Reply-To:': email}
        )

        mail.send()

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','estoque','imagem']