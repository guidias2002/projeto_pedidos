from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Pedido, Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re
from django import forms


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefone'].widget.attrs.update({'class':'mask-telefone'})

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if not len(telefone) == 15:
            raise ValidationError('Telefone inválido. Certifique-se que digitou o número correto.')
        else:
            return telefone

    def clean_email(self):
        email_cliente = self.cleaned_data['email']

        if User.objects.filter(email=email_cliente).exists():
            raise ValidationError('O email {} já esta em uso.'.format(email_cliente))
        elif re.search('^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]', email_cliente) is None:
            raise ValidationError('Email inválido.')
        else:
            return email_cliente
            

class CriarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
