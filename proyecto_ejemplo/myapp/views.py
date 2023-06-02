from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from myapp.models import Person, Pet


# Create your views here.
def index(request):
    print('estoy llamando al index')
    personas = Person.objects.all() # select * from personas 
    lista_personas = []
    for persona in personas:
        nombre_persona = "{} {}".format(persona.first_name, persona.last_name)
        lista_personas.append(nombre_persona)

    texto_respuesta =  """
        <h1> Hola mundo desde HttpResponse </h1>
        {}

    """.format(lista_personas)

    return HttpResponse(texto_respuesta)


# Create your views here.
def index_2(request):
    print('estoy llamando al index 2')
    template_name = 'myapp/index.html'
    context = {
        "some_text": "hola mundo desde la vista de django"
    }
    return render(request, template_name, context)


def lista_personas(request):
    template_name = 'myapp/personas_list.html'
    personas = Person.objects.all() # select * from personas 
    lista_personas = []
    for persona in personas:
        nombre_persona = "{} {}".format(persona.first_name, persona.last_name)
        lista_personas.append(nombre_persona)

    context = {
        "lista_personas": lista_personas
    }
    return render(request, template_name, context)

def lista_pet(request):
    template_name = 'myapp/pet_list.html'
    pets = Pet.objects.all() # select * from pet 
    lista_pet = []
    for pet in pets:
        nombre_pet= "{}".format(pet.name)
        lista_pet.append(nombre_pet)

    context = {
        "lista_pet": lista_pet
    }
    return render(request, template_name, context)

def detalle_persona(request, id):
    persona = Person.objects.filter(id=id).first() # select * from personas where id=1
    if persona:
        texto_respuesta =  """
            <h1> voy a buscar la persona con el id: {} </h1>
            <p> nombre: {} </p>
            <p> edad: {} </p>
            <p> nick_name: {} </p>
        """.format(id, persona.first_name, persona.age, persona.nick_name )
    else:
        texto_respuesta = """No se encuentra el registro con id: {}""".format(id)

    return HttpResponse(texto_respuesta)


def detalle_raza(request, raza_name):
    texto_respuesta =  """
        <h1> voy a buscar la informacion de la raza: {} </h1>
    """.format(raza_name)

    return HttpResponse(texto_respuesta)


def lista_personas_json(request):
    personas = Person.objects.all() # select * from personas 
    lista_personas = []
    for persona in personas:
        nombre_persona = "{} {}".format(persona.first_name, persona.last_name)
        lista_personas.append(nombre_persona)

    context = {
        "lista_personas": lista_personas
    }

    return JsonResponse(context)

## Actividad:
# 1) Realizar el enrutamiento dinamico para las mascotas,
# 2) Realizar el enrutamiento dinamico para las razas de las mascotas,

# 3) implementar la funcionalidad de las urls dinamicas: 
#
#    path('mascota/<int:id>', views.your_custom_view),
#    path('mascota/<int:id>/nota_medica', views.your_custom_view),
#
#   que deben visualiza la informacion correspondiente de las mascotas y sus notas medicas respectivamente
#   Deben hacer uso de la herencia de templates 
#   
# 4) agregar una nota por defecto en todas las visualizaciones de la vista #2 (la de las notas) que contenga
#    las recomendaciones generales basicas de un paciente. --> "estar pendiente a los cambios de temperatura, mantener hidratado etc etc "