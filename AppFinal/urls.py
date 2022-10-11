from django.urls import path
from AppFinal.views import *

urlpatterns = [
      path("", inicio, name= "Inicio"),
      path("curso/", curso, name= "Curso"),
      path("materia/", materia, name= "Materia"),
      path("cursoFormulario/", cursoFormulario, name="FormularioCurso"),
      path("busquedaCamada/", busquedaCamada, name= "BusquedaCamada"),
      path("resultados/", resultados, name= "ResultadoBusqueda4"),

]