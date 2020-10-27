from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('register/', views.register_user, name='register_user'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('perfil/', views.see_profile, name='perfil'),
    path('agregar_receta/', views.agregar_receta, name='agregar_receta'), 
    path('recetas/', views.recetas, name='recetas'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)