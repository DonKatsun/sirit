from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from ..models import *

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']  # Django utiliza 'username' en lugar de 'email' por defecto
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                response = redirect('/inventario')
                print(user.username)
                usruario = Usuarios.objects.filter(usuario=user.id).first()
                print(usruario)
                if usruario.id_rol.id != 1:
                    response.set_cookie('dependencia_usuario_id', usruario.id_dependencia.id, max_age=1800, secure=True, httponly=True)
                    response.set_cookie('dependencia_usuario', usruario.id_dependencia.nombre_dependencia, max_age=1800, secure=True, httponly=True)
                    response.set_cookie('secretaria_usuario_id', usruario.id_dependencia.id_secretaria.id, max_age=1800, secure=True, httponly=True)
                    response.set_cookie('secretaria_usuario', usruario.id_dependencia.id_secretaria.nombre_secretaria, max_age=1800, secure=True, httponly=True)
                    response.set_cookie('tipo', usruario.id_rol.id, max_age=1800, secure=True, httponly=True)
                return response
            else:
                return render(request, 'pages/login.html', {'form': form, 'error_message': 'Credenciales inválidas'})
    else:
        form = AuthenticationForm()
    return render(request, 'pages/login.html', {'form': form})


def logout_view(request):
    response = redirect('/login')
    response.delete_cookie('dependencia_usuario_id')
    response.delete_cookie('dependencia_usuario')
    response.delete_cookie('secretaria_usuario_id')
    response.delete_cookie('secretaria_usuario')
    response.delete_cookie('tipo')
    logout(request)
    # Redirigir a la página de inicio de sesión o a otra página después de cerrar sesión
    return response