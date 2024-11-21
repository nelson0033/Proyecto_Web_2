from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import datetime

from .models import VideojuegoRetro

# Create your views here.
def index(request):
    lista_videojuegos = VideojuegoRetro.objects.all()
    template = loader.get_template("index.html")
    context = {"videojuegos":lista_videojuegos}
    return HttpResponse(template.render(context,request))

def vista_detalle(request, id):
    detalle_videojuego = VideojuegoRetro.objects.get(id=id)
    template = loader.get_template("detail.html")
    context = {"videojuego":detalle_videojuego}
    return HttpResponse(template.render(context,request))