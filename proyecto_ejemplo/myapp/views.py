from django.shortcuts import render

# Create your views here.

age = 25

age = "25; mi otra consulata SQL"

sql = '''
    SELECT *
    FROM myapp_person
    WHERE age={}
    Limit 1;
'''.format(age)

person = Person.objects.filter(age=age).first()