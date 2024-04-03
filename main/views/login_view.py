from django.shortcuts import render, redirect

def login(request):
    #conmutadores = Conmutadores.objects.all()
    return render(request, 'pages/login.html', )