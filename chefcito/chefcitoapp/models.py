from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    descripcion = models.TextField(blank = True)
    fecha_nacimiento = models.DateField(null = True, blank = True)
    class Meta:
        unique_together = ['email']
    avatar = models.FileField(upload_to='avatars/',blank=True, null= True)
    experiencias = [('Solo Maruchan','Solo Maruchan'),('Primeros platos','Primeros platos'), ('Cocinero/a/e Amateur','Cocinero/a/e Amateur'),('Chef Profesional','Chef Profesional')]
    experiencia = models.CharField(max_length=100,choices=experiencias)
