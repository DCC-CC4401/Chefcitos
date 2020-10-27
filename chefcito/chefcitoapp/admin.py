from django.contrib import admin
from .models import User, Receta, Ingrediente

admin.site.register(User)
admin.site.register(Receta)
admin.site.register(Ingrediente)
