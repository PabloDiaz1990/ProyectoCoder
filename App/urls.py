from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('cursoForm', views.curso_formulario, name="CursoFormulario"),
    path('cursoBusqueda', views.curso_busqueda, name="CursoBusqueda"),
    path('cursoBuscar', views.curso_buscar),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('profesores', views.profesores, name="Profesores")
]