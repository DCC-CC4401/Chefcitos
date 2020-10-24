from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.hashers import check_password
from .models import User, Ingrediente, Receta, CalificaReceta
from django.contrib.auth import authenticate, login,logout

def inicio(request):
    if request.method == "GET":
        return render(request, "chefcitoapp/index.html")


def register_user(request):
    if request.method == 'GET': #Si estamos cargando la página
        return render(request, "todoapp/register_user.html") #Mostrar el template

    elif request.method == 'POST': #Si estamos recibiendo el form de registro

        #Tomar los elementos del formulario que vienen en request.POST
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']
        apodo = request.POST['apodo']
        pronombre = request.POST['pronombre']
        mail = request.POST['mail']

        #Crear el nuevo usuario
        user = User.objects.create_user(username=nombre, password=contraseña, email=mail, apodo=apodo, pronombre=pronombre)

        #Redireccionar la página /tareas
        return HttpResponseRedirect('/tareas')

def login_user(request):
    if request.method == 'GET':
        return render(request,"chefcitoapp/login.html")
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        usuario = authenticate(username=username,password=contraseña)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect('/tareas')
        else:
            return HttpResponseRedirect('/register')


def logout_user(request):
   logout(request)
   return HttpResponseRedirect('/tareas')

# Create your views here.


def see_profile(request):
    """
       Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

       Use the login name and a hash of the password. For example:

       ADMIN_LOGIN = 'admin'
       ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
       """
    def authenticate(self, request, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


    if request.method=='GET':
        if request.user.is_authenticated:
            username = request.user.username
            the_profile=get_user(username)
            return render(request, 'chefcitoapp\perfil.html',the_profile)

        else:
            html="<html><body><h1>No ha iniciado sesion</h1>.</body></html>"
            return HttpResponse(html)
