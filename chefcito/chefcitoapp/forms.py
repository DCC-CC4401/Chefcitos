from django import forms
from .models import User, Ingrediente, CalificaReceta, Receta
from django.db import models
from django.utils import timezone

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['first_name', 'last_name', 'fecha_nacimiento','username', 'password', 'email', 'descripcion', 'experiencia', 'avatar', 'vegano', 'vegetariano', 'celiaco', 'diabetico', 'intolerancia_lactosa']
        
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    first_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidgets(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), min_length=6, max_length=12)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    descripcion=forms.Textarea()
    experiencias = [('Solo Maruchan', 'Solo Maruchan'), ('Primeros platos', 'Primeros platos'),
                    ('Cocinero/a/e Amateur', 'Cocinero/a/e Amateur'), ('Chef Profesional', 'Chef Profesional')]

    experiencia = forms.ChoiceField(widget=forms.Select(), choices=experiencias)
    vegetariano=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    vegano = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    diabetico = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    celiaco = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    intolerancia_lactosa = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))



