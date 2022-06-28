from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('cursoForm', views.curso_formulario, name="CursoFormulario"),
    path('cursoBusqueda', views.curso_busqueda, name="CursoBusqueda"),
    path('cursoBuscar', views.curso_buscar),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('estudianteForm', views.estudiante_formulario, name="EstudianteFormulario"),
    path('estudianteBusqueda', views.estudiante_busqueda, name="EstudianteBusqueda"),
    path('estudianteBuscar', views.estudiante_buscar),
    path('profesores', views.profesores, name="Profesores"),
    path('profesorForm', views.profesor_formulario, name="ProfesorFormulario"),
    path('profesorBusqueda', views.profesor_busqueda, name="ProfesorBusqueda"),
    path('profesorBuscar', views.profesor_buscar)
]