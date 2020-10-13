from django.db import models
from django.utils import timezone



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
    nombre_usuario = models.ForeignKey(Usuario, default="general", on_delete=models.CASCADE)
    receta_nombre= models.CharField(primary_key=True, max_length=250)

    preparacion=models.TextField(max_length=1300)
    duracion = models.TimeField()
    receta_foto=models.TextField(max_length=200)
    fecha_publ=models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    descripcion=models.TextField()
    ingrediente=models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.receta_nombre

# Create your models here.

