from django.shortcuts import render
from .models import Departamento

# Create your views here.

def index(request):

    return render(request,"index.html")

def quienesSomos(request):
    return render(request,"quienesSomos.html")

def donaciones(request):
    return render(request,"donaciones.html")

def departamentos(request):

    data = Departamento.objects.all()

    info = {
        "datos" : data
    }
    return render(request,"departamentos.html",context=info)

def contacto(request):
    return render(request,"contacto.html")

def ubicaciones(request):
    return render(request,"ubicaciones.html")