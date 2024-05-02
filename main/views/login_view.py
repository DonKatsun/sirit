from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']  # Django utiliza 'username' en lugar de 'email' por defecto
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/inventario')
            else:
                return render(request, 'pages/login.html', {'form': form, 'error_message': 'Credenciales inválidas'})
    else:
        form = AuthenticationForm()
    return render(request, 'pages/login.html', {'form': form})


def logout_view(request):
    logout(request)
    # Redirigir a la página de inicio de sesión o a otra página después de cerrar sesión
    return redirect('/login')