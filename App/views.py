from django.shortcuts import render
from django.http import HttpResponse
from App.models import *

def inicio(request):
    return render(request, "App/inicio.html")

def cursos(request):
    return render(request, "App/cursos.html")

def profesores(request):
    return render(request, "App/profesores.html")

def estudiantes(request):
    return render(request, "App/estudiantes.html")