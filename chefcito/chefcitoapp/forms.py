from django import forms
from .models import User, Ingrediente, CalificaReceta, Receta
from django.db import models

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['first_name', 'last_name', 'username', 'password', 'email', 'descripcion', 'avatar']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    password= forms.CharField(widget=forms.PasswordInput, min_length=6, max_length=12)
    experiencias = [('Solo Maruchan', 'Solo Maruchan'), ('Primeros platos', 'Primeros platos'),
                    ('Cocinero/a/e Amateur', 'Cocinero/a/e Amateur'), ('Chef Profesional', 'Chef Profesional')]
    experiencia = forms.ChoiceField(widget=forms.RadioSelect, choices=experiencias)
    fecha_nacimiento =  forms.DateField(widget=forms.SelectDateWidget)
