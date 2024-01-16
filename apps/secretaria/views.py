# from django.http import JsonResponse, HttpResponse
from .models import Estudiante
from django.shortcuts import render, redirect, get_object_or_404
from .forms import InsertarEstudiante, modificarForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def welcome(request):
   user = User.objects.get(username=request.user.username)
   return render(request, 'index.html', {
      'user': user
   })
@login_required
def listarEstudiantes(request):
   # estudiantes = list(Estudiante.objects.values())
   estudiantes = Estudiante.objects.all()
   return render(request, 'estudiante/listar_estudiantes.html', {
      'estudiantes': estudiantes
   })
@login_required
def crearEstudiante(request):
   num_registros_e=Estudiante.objects.count()
   if num_registros_e < 10 and request.method == 'GET':
      return render(request, 'estudiante/insertar_estudiante.html', {
      'form': InsertarEstudiante()
   },)

   if num_registros_e == 10 and request.method == 'GET' :
      return render(request, 'estudiante/insertar_estudiante.html', {'error':'Haz alcanzado el número maximo de registros en el sistema'})

   else:

      Estudiante.objects.create(
         nombre=request.POST['nombre'],
         apellidos=request.POST['apellidos'],
         sexo=request.POST['sexo'],
         ci=request.POST['ci'],
         dir=request.POST['dir'],
         tel=request.POST['tel'],
         grupo=request.POST['grupo'],
         anno=request.POST['anno'],
      )
      return redirect('estudiantes')

   
@login_required
def modificarEstudiante(request, id):
   if request.method == 'GET':
      estudiante = get_object_or_404(Estudiante, ci=id)
      form = modificarForm(instance=estudiante)
      return render(request, 'estudiante/modificar_estudiante.html', {
         'estudiante' : estudiante, 'form' : form
      })
   else :
      try:
         estudiante = get_object_or_404(Estudiante, ci=id)
         form = modificarForm(request.POST, instance=estudiante)
         form.save()
         return redirect('estudiantes')
      except ValueError:
         return render(request, 'estudiante/modificar_estudiante.html', {
         'estudiante' : estudiante, 'form' : form, 'error': 'Error actualizando el estudiante'
      })
@login_required
def eliminarEstudiante(request, id):
   estudiante = get_object_or_404(Estudiante, ci=id)
   if request.method == 'POST':
      estudiante.delete()
      return redirect('estudiantes')

 