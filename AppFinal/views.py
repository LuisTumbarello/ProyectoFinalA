from django.shortcuts import render
from django.http import HttpResponse
from AppFinal.models import *
from AppFinal.forms import *

# Create your views here.
def inicio(request):
    return render(request, "AppFinal/inicio.html")

def curso(request):
    cursoa = Curso(nombre="Luis", camada="1")
    cursoa.save()

    return render(request, "AppFinal/curso.html")

def materia(request):
    materiaa = Materia(nombre="Python", inicio="20221001")
    return render(request, "AppFinal/materia.html")

def cursoFormulario(request):

    if request.method == "POST":

        formulario1= CursoFormulario(request.POST)

        if formulario1.is_valid():
            info= formulario1.cleaned_data
            curso= Curso(nombre=info["curso"], camada=info["camada"]) 
            curso.save()
            return render(request, "AppFinal/inicio.html")
    
    else:
        formulario1= CursoFormulario()

    return render(request, "AppFinal/cursoFormulario.html", {"form1":formulario1})

def busquedaCamada(request):
    
    return render(request, "AppFinal/inicio.html")

def resultados(request):

    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppFinal/inicio.html", {"cursos":cursos, "camada":camada})
    
    else:

        respuesta = "No enviaste Datos"

    return HttpResponse(respuesta)

    return HttpResponse(f"Estas buscando la camada numero: {request.GET['camada']}")