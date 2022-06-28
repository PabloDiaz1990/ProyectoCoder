from django.shortcuts import render
from django.http import HttpResponse
from App.models import *
from App.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
from django.db.models import Q

def inicio(request):
    return render(request, "App/inicio.html")

def cursos(request):
    return render(request, "App/cursos.html")

def curso_formulario(request):
    if request.method == 'POST':
        form = CursoFormulario(request.POST)
        print(form)
        
        if form.is_valid:
            info = form.cleaned_data
            curso = Curso(nombre=info['curso'], numero_curso=info['numero_curso'])
            curso.save()

            return render(request, "App/cursos.html")
    else:

        form = CursoFormulario()
    
    return render(request, "App/curso_form.html", {"form":form})

def curso_busqueda(request):
    return render(request, "App/curso_form_buscar.html")

def curso_buscar(request):
    if request.GET['num_curso']:
        num_curso = request.GET['num_curso']
        curso = Curso.objects.filter(numero_curso__icontains=num_curso)

        return render(request, "App/curso_resp_busqueda.html", {"curso":curso, "num_curso":num_curso})
    else:
        resp = "Dato sin ingresar"

    return HttpResponse(resp)

def profesores(request):
    return render(request, "App/profesores.html")

def profesor_formulario(request):
    if request.method == 'POST':
        form = ProfesorFormulario(request.POST)
        print(form)
        
        if form.is_valid:
            info = form.cleaned_data
            profesor = Profesor(nombre=info['nombre'], apellido=info['apellido'], email=info['email'], profesion=info['profesion'])
            profesor.save()

            return render(request, "App/profesores.html")
    else:

        form = ProfesorFormulario()
    
    return render(request, "App/profesor_form.html", {"form":form})

def profesor_busqueda(request):
    return render(request, "App/profesor_form_buscar.html")

def profesor_buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        profesor = Profesor.objects.filter(Q(nombre__icontains=nombre) | Q(apellido__icontains=nombre) | Q(profesion__icontains=nombre) | Q(email__icontains=nombre))

        return render(request, "App/profesor_resp_busqueda.html", {"profesor":profesor, "nombre":nombre})
    else:
        resp = "Dato sin ingresar"

    return HttpResponse(resp)

def estudiantes(request):
    return render(request, "App/estudiantes.html")

def estudiante_formulario(request):
    if request.method == 'POST':
        form = EstudianteFormulario(request.POST)
        print(form)
        
        if form.is_valid:
            info = form.cleaned_data
            estudiante = Estudiante(nombre=info['nombre'], apellido=info['apellido'], email=info['email'])
            estudiante.save()

            return render(request, "App/estudiantes.html")
    else:

        form = EstudianteFormulario()
    
    return render(request, "App/estudiante_form.html", {"form":form})

def estudiante_busqueda(request):
    return render(request, "App/estudiante_form_buscar.html")

def estudiante_buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        estudiante = Estudiante.objects.filter(Q(nombre__icontains=nombre) | Q(apellido__icontains=nombre) | Q(email__icontains=nombre))

        return render(request, "App/estudiante_resp_busqueda.html", {"estudiante":estudiante, "nombre":nombre})
    else:
        resp = "Dato sin ingresar"

    return HttpResponse(resp)