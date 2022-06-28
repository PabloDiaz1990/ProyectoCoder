from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    numero_curso = forms.IntegerField()