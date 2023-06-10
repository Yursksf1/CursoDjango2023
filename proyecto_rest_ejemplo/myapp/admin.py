from django.contrib import admin

# Register your models here.
from myapp.models import Especie, Mascota

admin.site.register(Especie)
admin.site.register(Mascota)