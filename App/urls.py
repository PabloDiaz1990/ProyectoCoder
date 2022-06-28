from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('profesores', views.profesores, name="Profesores")
]