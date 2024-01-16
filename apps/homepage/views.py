from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

def iniciarSesion(request):
   if request.method == 'GET':
      return render(request, 'login.html')
   else :
      user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
      if user is None:
         print(request.POST)
         return render(request, 'login.html', {
            'error': 'Usuario o contraseña incorrecto'
         })
      else:
         login(request, user)
         return redirect('index')

def cerrarSesion(request):
   logout(request)
   return redirect('signup')
      

