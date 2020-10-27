from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.hashers import check_password
from .models import User, Ingrediente, Receta, CalificaReceta
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.password_validation import validate_password
from .forms import UserForm

def inicio(request):
    if request.method == "GET":
        return render(request, "chefcitoapp/index.html")



def login_user(request):
    if request.method == 'GET':
        return render(request,"chefcitoapp/login.html")
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        usuario = authenticate(username=username,password=contraseña)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/register')


def logout_user(request):
   logout(request)
   return HttpResponseRedirect('/')

# Create your views here.


def see_profile(request):
    def get_user(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


    if request.method=='GET':
        if request.user.is_authenticated:
            username = request.user.id
            form=get_user(username)
            return render(request, 'chefcitoapp/perfil.html',{'form':form})

        else:
            html="<html><body><h1>No ha iniciado sesion</h1>.</body></html>"
            return HttpResponse(html)



def editar_perfil(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            the_profile = request.user
            return render(request, 'chefcitoapp/editar_perfil.html', {'form': the_profile})

        if request.method == 'POST':
            form = UserForm(request.POST or None)
            if form.is_valid():
                the_profile = request.user
                the_profile.first_name = form.cleaned_data["first_name"]
                the_profile.last_name = form.cleaned_data["last_name"]
                the_profile.password = form.cleaned_data["password"]
                the_profile.email = form.cleaned_data["email"]
                the_profile.fecha_nacimiento = form.cleaned_data["fecha_nacimiento"]
                the_profile.experiencia = form.cleaned_data["experiencia"]
                the_profile.descripcion = form.cleaned_data["descripcion"]

                the_profile.save()
                return render(request, 'chefcitoapp/index.html')

            return render(request, 'chefcitoapp/editar_perfil.html', {'form': form})


def register_user(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            form = UserForm()
            return render(request, 'chefcitoapp/registrarse.html', {'form': form})

    if request.method=='POST':
        form = UserForm(request.POST or None)


        if form.is_valid():
            user = form.save()
            return render(request, 'chefcitoapp/index.html')

        return render(request, 'chefcitoapp/registrarse.html', {'form':form})


def agregar_receta(request):

    ingredientes = Ingrediente.objects.all() 
     
    if request.method == "GET":
        return render(request, "chefcitoapp/agregar_receta.html", {"ingredientes": ingredientes})
 
    elif request.method == 'POST': #Si estamos recibiendo el form de registro
        if "recetaAdd" in request.POST: 
            if request.user.is_authenticated:
                receta_nombre = request.POST['receta_nombre']
                preparacion = request.POST['preparacion']
                duracion = request.POST['duracion']
                receta_foto = request.POST['receta_foto']
                descripcion = request.POST['descripcion']
                ingredientes_receta = request.POST['ingredientes[]']

                receta = Receta(receta_nombre=receta_nombre, preparacion=preparacion, duracion=duracion, receta_foto=receta_foto, descripcion=descripcion, ingrediente=ingredientes_receta, nombre_usuario=request.user)
                receta.save() 

            return HttpResponseRedirect('/agregar_receta')


def recetas(request):

    recetas = Receta.objects.all() 

    if request.method == "GET":
        return render(request, "chefcitoapp/recetas.html", {"recetas": recetas})
    
