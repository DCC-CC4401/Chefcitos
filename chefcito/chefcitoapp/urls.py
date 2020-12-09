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
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('agregar_receta/', views.agregar_receta, name='agregar_receta'), 
    path('todas_recetas/', views.todas_recetas, name='recetas'),
    path('receta/<int:receta_id>/', views.vista_receta, name='ver_receta'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)