from django.db import models

class Estudiante(models.Model):
   nombre = models.CharField(max_length=20)
   apellidos = models.CharField(max_length=40)
   sexo = models.CharField(max_length=1, choices = (
      ('M', 'M'),
      ('F', 'F')
   ))
   ci = models.IntegerField()
   dir = models.CharField(max_length=100)
   tel = models.IntegerField()
   grupo = models.IntegerField()
   anno = models.CharField(max_length=1, choices= (
      ('1', '1'),
      ('2', '2'),
      ('3', '3'),
      ('4', '4'),
      ('5', '5')
   ))

   def __str__(self):
      return self.nombre