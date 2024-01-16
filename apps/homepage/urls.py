from django.urls import path
from . import views

urlpatterns = [   
   path('', views.iniciarSesion, name='signup'),
   path('logout/', views.cerrarSesion, name='logout'),
]
