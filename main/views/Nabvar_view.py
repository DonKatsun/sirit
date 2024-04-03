from django.shortcuts import render, redirect

def Nabvar (request):
    #conmutadores = Conmutadores.objects.all()
    return render(request, 'pages/Nabvar.html', )