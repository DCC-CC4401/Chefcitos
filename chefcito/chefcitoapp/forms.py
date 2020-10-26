from django import forms
from .models import User, Ingrediente, CalificaReceta, Receta

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['first_name', 'last_name', 'username', 'password', 'email', 'descripcion', 'fecha_nacimiento', 'avatar', 'experiencia']