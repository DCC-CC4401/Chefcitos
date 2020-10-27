from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    descripcion = models.TextField(blank = True)
    fecha_nacimiento = models.DateField(null = True, blank = True)
    class Meta:
        unique_together = ['email']
    avatar = models.FileField(upload_to='avatars/',blank=True, null= True)
    experiencias = [('Solo Maruchan','Solo Maruchan'),('Primeros platos','Primeros platos'), ('Cocinero/a/e Amateur','Cocinero/a/e Amateur'),('Chef Profesional','Chef Profesional')]
    exp = []
    for i in experiencias:
        exp.append(i[0])
    experiencia = models.CharField(max_length=100,choices=experiencias)

    # elecciones = [(1,'Si'),(0,'No')]
    vegano = models.BooleanField(default=False)
    vegetariano = models.BooleanField(default=False)
    diabetico = models.BooleanField(default=False)
    celiaco = models.BooleanField(default=False)
    intolerancia_lactosa = models.BooleanField(default=False)


class Ingrediente(models.Model):
    ingrediente_id=models.AutoField(primary_key=True)
    ingrediente_nombre=models.CharField(max_length=20)
    vegano=models.BooleanField(default=False)
    vegetariano=models.BooleanField(default=False)
    diabetico=models.BooleanField(default=False)
    celiaco=models.BooleanField(default=False)
    int_lactosa=models.BooleanField(default=False)

    def __str__(self):
        return self.ingrediente_id



class Receta(models.Model):
    nombre_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    receta_nombre= models.CharField(primary_key=True, max_length=250)

    preparacion=models.TextField(max_length=1300)
    duracion = models.TimeField()
    receta_foto=models.ImageField(upload_to='fotos_recetas')
    fecha_publ=models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    descripcion=models.TextField()
    ingrediente=models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.receta_nombre


class CalificaReceta(models.Model):
    nombre_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    receta_id = models.ForeignKey(Receta, on_delete=models.CASCADE)
    nota=models.DecimalField(decimal_places=1, max_digits=3)