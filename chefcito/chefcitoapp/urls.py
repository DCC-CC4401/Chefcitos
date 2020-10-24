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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)