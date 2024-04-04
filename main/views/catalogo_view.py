from django.shortcuts import render, redirect

def catalogo (request):
    #conmutadores = Conmutadores.objects.all()
    return render(request, 'pages/Catalogo.html', )