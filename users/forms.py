from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Seu e-mail',
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza os campos padrão de senha
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Senha',
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirme a senha',
            'class': 'form-control'
        })
