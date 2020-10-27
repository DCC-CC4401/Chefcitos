from django import forms
from .models import User, Ingrediente, CalificaReceta, Receta
from django.db import models
from django.utils import timezone

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['first_name', 'last_name', 'fecha_nacimiento','username', 'password', 'email', 'descripcion', 'experiencia', 'avatar', 'vegano', 'vegetariano', 'celiaco', 'diabetico', 'intolerancia_lactosa']

        widget = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'experiencia': forms.Select(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'experiencia': forms.Select(attrs={'class': 'form-control'}),
            'vegetariano': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'vegano': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'celiaco': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'diabetico': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'intolerancia_lactosa': forms.CheckboxInput(attrs={'class': 'form-control'}),
        
        }
        
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
    fecha_nacimiento =  forms.DateField(widget=forms.SelectDateWidget(years = range(1990, timezone.now().year+1)))

