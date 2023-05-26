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