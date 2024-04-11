from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ..forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            contrasenia = form.cleaned_data['contrasenia']
            # Autenticar al usuario utilizando los nombres de los campos correctos
            usuario = authenticate(request, email=email, password=contrasenia)
            if usuario is not None:
                login(request, usuario)
                # Redirige al usuario a la página de inicio o a donde quieras que vaya después del inicio de sesión
                return redirect('conmutador')
            else:
                # El usuario no pudo ser autenticado, mostrar un mensaje de error
                return render(request, 'pages/login.html', {'form': form, 'error': 'Credenciales inválidas.'})
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})

