from django import forms
from django.forms import ModelForm
from .models import Estudiante

class InsertarEstudiante(forms.Form):
   nombre = forms.CharField(label='Nombre', max_length=20)
   apellidos = forms.CharField(label='Apellidos', max_length=40)
   sexo = forms.ChoiceField(label='Sexo', choices = (
      ('M', 'M'),
      ('F', 'F')
   ))
   ci = forms.IntegerField(label='Carnet de identidad')
   dir = forms.CharField(label='Dirección', max_length=100)
   tel = forms.IntegerField(label='Número de telefónico')
   grupo = forms.IntegerField(label='Grupo')
   anno = forms.ChoiceField(label='Año', choices= (
      ('1', '1'),
      ('2', '2'),
      ('3', '3'),
      ('4', '4'),
      ('5', '5')
   ))

class modificarForm(ModelForm):
   class Meta:
      model = Estudiante
      fields = ['nombre', 'apellidos', 'sexo', 'ci', 'dir', 'tel', 'grupo', 'anno']