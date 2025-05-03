from django import forms
from .models import Videojuego

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'descripcion', 'imagen', 'categoria', 'precio']
