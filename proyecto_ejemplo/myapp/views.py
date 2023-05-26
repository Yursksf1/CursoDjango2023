from django.shortcuts import render, HttpResponse
from myapp.models import Person


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
    return render(request, template_name)