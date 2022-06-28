from django.db import models

# Definición de clases y sus campos
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    numero_curso = models.IntegerField()

    def __str__(self):
        return f"Nombre Curso: {self.nombre} - Número Curso: {self.numero_curso}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre Estudiante: {self.nombre} - Apellido Estudiante: {self.apellido} - email: {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesor: {self.profesion}"
