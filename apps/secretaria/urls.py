from django.urls import path
from . import views

urlpatterns = [
   path('', views.welcome, name='index'),
   path('estudiantes/', views.listarEstudiantes, name='estudiantes'),
   path('insertar_estudiante/', views.crearEstudiante, name='insertar_estudiante'),
   
   path('modificar_estudiante/<int:id>', views.modificarEstudiante, name='modificar_estudiante'),
   path('modificar_estudiante/<int:id>/eliminar', views.eliminarEstudiante, name='eliminar_estudiante'),
]
