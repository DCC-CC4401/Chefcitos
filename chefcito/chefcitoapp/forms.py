from django import forms
from .models import User, Ingrediente, CalificaReceta, Receta, RecetaIngrediente
from django.db import models
from django.utils import timezone
from django.forms import formset_factory


class DateInputtrue(forms.DateInput):
    input_type = 'date'

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['first_name', 'last_name', 'fecha_nacimiento','username', 'password', 'email', 'descripcion', 'experiencia','vegano', 'vegetariano', 'celiaco', 'diabetico', 'intolerancia_lactosa', 'avatar']

        def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            self.fields['first_name', 'last_name', 'fecha_nacimiento', 'descripcion', 'experiencia', 'vegano', 'celiaco', 'diabetico', 'intolerancia_lactosa', 'avatar'].required = False

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Las contraseñas no coinciden"
            )

    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese su nombre..'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese su apellido..'}))
    fecha_nacimiento = forms.DateField(required=False, widget=DateInputtrue(format='%m/%d/%Y',
                               attrs={'class': 'form-control datepicker'}))

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el nombre de usuario..'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Ingrese la contaseña..'}), min_length=6, max_length=12)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirme la contaseña..'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Ingrese su email..'}))
    descripcion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':"3",'cols':'70' , 'placeholder':'Ingrese una descripcion breve..'}))
    experiencias = [('Solo Maruchan', 'Solo Maruchan'), ('Primeros platos', 'Primeros platos'),
                    ('Cocinero/a/e Amateur', 'Cocinero/a/e Amateur'), ('Chef Profesional', 'Chef Profesional')]


    experiencia = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'custom-select'}), choices=experiencias)
    vegetariano = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    vegano = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    diabetico = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    celiaco = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    intolerancia_lactosa = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    avatar=forms.FileField(required=False)



class RecetaForm(forms.ModelForm):
    class Meta:
        model= Receta
        fields = ['receta_nombre', 'preparacion','duracion', 'descripcion','receta_foto', 'vegetariano', 'receta_foto','vegano', 'diabetico', 'celiaco', 'int_lactosa']

    def __init__(self, *args, **kwargs):
        super(RecetaForm, self).__init__(*args, **kwargs)


    def save(self, **kwargs):
        user = kwargs.pop('user')
        instance = super(RecetaForm, self).save(**kwargs)
        instance.nombre_usuario = user
        instance.save()
        return instance



    receta_nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese nombre de la receta..'}))
    duracion = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese duración..'}))

    preparacion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':"3",'cols':'70' , 'placeholder':'Ingrese los pasos de preparación..'}))

    #ingrediente = forms.ModelMultipleChoiceField(
    #    queryset=Ingrediente.objects.all(),
    #    widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    #    #widget = forms.SelectMultiple(attrs={'class': 'form-control'})
    #)

    descripcion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':"3",'cols':'70' , 'placeholder':'Ingrese una descripcion breve..'}))
    receta_foto = forms.FileField(widget=forms.FileInput())

    vegetariano = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    vegano = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    diabetico = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    celiaco = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    int_lactosa = forms.BooleanField(required=False,
                                              widget=forms.CheckboxInput(attrs={'class': 'form-control'}))

class RecetaIngredienteForm(forms.ModelForm):
    class Meta:
        model= RecetaIngrediente
        fields = ['ingrediente_id','medida', 'unidad']

    def __init__(self, *args, **kwargs):
        super(RecetaIngredienteForm, self).__init__(*args, **kwargs)


    def save(self, **kwargs):
       receta = kwargs.pop('receta')
       instance = super(RecetaIngredienteForm, self).save(**kwargs)
       instance.receta_id = receta
       instance.save()



    ingrediente_id = forms.ModelChoiceField( 
       queryset=Ingrediente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    medida = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese unidad de medida.'}))

    unidad = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad.'}))


RecetaIngredienteFormSet=formset_factory(RecetaIngredienteForm)



class IngredienteForm(forms.ModelForm):
    class Meta:
        model= Ingrediente
        fields = ['ingrediente_nombre']

    ingrediente_nombre = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el nombre del ingrediente..'}))