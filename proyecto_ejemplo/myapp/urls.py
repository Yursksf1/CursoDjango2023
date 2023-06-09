"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

app_name = "app" 
urlpatterns = [
    path('', views.index),
    path('home', views.index_2),
    path('lista_personas', views.lista_personas),
    path('lista_pet', views.lista_pet),
    path('lista_personas_json', views.lista_personas_json),
    # path('lista_raza', views.lista_personas),
    path('personas/<int:id>', views.detalle_persona),
    path('razas/<str:raza_name>', views.detalle_raza),
    path('mascota/<int:id>/nota_medica', views.your_custom_view),



]
