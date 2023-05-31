from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    # nacionalidad = models.CharField(max_length=30, blank=True, null=True)


    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)


class Pet(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return "{} - {}".format(self.name, self.person)
    

"""
Actividad:
1) Crear una tabla para las especies de las mascotas (PET)
    Ejemplo una mascota puede ser, un perro, o un gato, o un ave.. 
    esta tabla debe contener el nombre de la especie, y 
    debe existir una relacion entre una mascota y la especie a la que pertenece. 

2) Crear otra tabla que guarde las "notas u observaciones" de las mascotas Ejemplo:
    flofy: tiene una nota medica, que dice que no puede correr a medio dia
    canariam, tiene una observacion, que recomienda darle una comida especial..
"""




class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline