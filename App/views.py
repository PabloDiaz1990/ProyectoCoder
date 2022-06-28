from django.shortcuts import render
from django.http import HttpResponse
from App.models import *
from App.forms import CursoFormulario

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
        #resp = f"Buscando el número de curso: {request.GET['num_curso']}"
        num_curso = request.GET['num_curso']
        curso = Curso.objects.filter(numero_curso__icontains=num_curso)

        return render(request, "App/curso_resp_busqueda.html", {"curso":curso, "num_curso":num_curso})
    
    else:
        resp = "Dato sin ingresar"

    return HttpResponse(resp)

def profesores(request):
    return render(request, "App/profesores.html")

def estudiantes(request):
    return render(request, "App/estudiantes.html")