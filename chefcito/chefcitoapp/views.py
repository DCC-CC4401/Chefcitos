from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.hashers import check_password
from .models import User, Ingrediente, Receta, CalificaReceta
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.password_validation import validate_password
from .forms import UserForm, RecetaForm
from datetime import *
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AVATAR_ROOT = os.path.join(BASE_DIR, 'media')
def inicio(request):
    if request.method == "GET":
        pass
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
            messages.success(request, 'Bienvenid@ ' + usuario.username)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Error al iniciar sesión')
            return HttpResponseRedirect(request.path)



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

            #form = UserForm(request.POST or None)
            #if form.is_valid():
            the_profile = request.user
            if 'fotoperfil-edit' in request.POST: #Edit Picture
            
                if request.FILES['adjunto']:
                    old = the_profile.avatar
                    the_profile.avatar = request.FILES['adjunto']
                    the_profile.avatar.name = the_profile.username + "##" + str(datetime.now()) +".png"
                    print(the_profile.avatar.url)
                    if str(old) != '':
                        try:
                            os.remove(os.path.join(AVATAR_ROOT, old.name))
                        except:
                            print("error")
                    messages.success(request, 'Foto de perfil actualizada! :D')
                the_profile.save()
                return HttpResponseRedirect(request.path)
            else:
                the_profile = request.user
                the_profile.first_name = request.POST["Nombre"]
                the_profile.last_name = request.POST["Apellido"]
                the_profile.fecha_nacimiento = request.POST["Nacimiento"]
                the_profile.experiencia = request.POST["Experiencia"]
                the_profile.descripcion = request.POST["Descripcion"]


                the_profile.vegetariano = bool(request.POST.get('Vegetariano', False))
                the_profile.vegano = bool(request.POST.get('Vegano', False))
                the_profile.diabetico = bool(request.POST.get('Diabetico', False))
                the_profile.celiaco = bool(request.POST.get('Celiaco', False))
                the_profile.intolerancia_lactosa = bool(request.POST.get('int_lactosa', False))
                
            the_profile.save()
            messages.success(request, 'Perfil actualizado! c:')
            return HttpResponseRedirect('/perfil') # al guardar redirige al perfil(???) 



def register_user(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            form = UserForm()
            return render(request, 'chefcitoapp/registrarse.html', {'form': form})

    if request.method=='POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/')

        return render(request, 'chefcitoapp/registrarse.html', {'form':form})


def agregar_receta(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            form = RecetaForm()
            return render(request, 'chefcitoapp/agregar_receta.html', {'form': form})

    if request.method == 'POST':
        if request.user.is_authenticated:

            if 'ingre' in request.POST: 
                print("OLA")
                nombre = request.POST["ingrediente_nombre"]
                vegetariano = bool(request.POST.get('Vegetariano', False))
                vegano = bool(request.POST.get('Vegano', False))
                diabetico = bool(request.POST.get('Diabetico', False))
                celiaco = bool(request.POST.get('Celiaco', False))
                intolerancia_lactosa = bool(request.POST.get('int_lactosa', False))
                nuevo_ingre = Ingrediente(ingrediente_nombre=nombre, vegano=vegano, vegetariano=vegetariano, diabetico=diabetico, celiaco=celiaco, int_lactosa= intolerancia_lactosa)
                nuevo_ingre.save()

            else:
                print("CHAO")
                form = RecetaForm(request.POST or None)

                if form.is_valid():
                    form.save(user=request.user, commit=False)
                    return HttpResponseRedirect('/')

                return render(request, 'chefcitoapp/agregar_receta.html', {'form': form})


def todas_recetas(request):
    recetas = Receta.objects.all()
    vegano = False
    vegetariano = False
    diabetico = False
    celiaco = False
    int_lactosa = False

    if request.method == 'POST':
        if 'filtrar' in request.POST: #Edit Picture
            vegetariano = bool(request.POST.get('Vegetariano', False))
            vegano = bool(request.POST.get('Vegano', False))
            diabetico = bool(request.POST.get('Diabetico', False))
            celiaco = bool(request.POST.get('Celiaco', False))
            int_lactosa = bool(request.POST.get('int_lactosa', False))
            # recetas = Receta.objects.filter(vegano__gte=True, vegetariano__gte=True)
            if vegetariano:
                recetas = recetas.filter(vegetariano__gte = True)
            if vegano:
                recetas = recetas.filter(vegano__gte = True)
            if diabetico:
                recetas = recetas.filter(diabetico__gte = True)
            if celiaco:
                recetas = recetas.filter(celiaco__gte = True)
            if int_lactosa:
                recetas = recetas.filter(int_lactosa__gte = True)
            
    return render(request, "chefcitoapp/todas_recetas.html", {"receta": recetas, "vegano": vegano, "vegetariano": vegetariano, "diabetico": diabetico, "celiaco": celiaco, "int_lactosa": int_lactosa})

    
def vista_receta(request, receta_id):
    try:
        receta=Receta.objects.get(receta_id=receta_id)
    except Receta.DoesNotExist:
        receta = None

    if receta!=None:
        return render(request, 'chefcitoapp/vista_receta_alt.html', {"receta": receta})
    else:
        return render(request, 'chefcitoapp/receta_no_valida.html')

