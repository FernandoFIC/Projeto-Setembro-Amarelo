from django.forms import ModelForm
from django import forms
from blog.models import Contato

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu Email'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sua Mensagem'}),
        }