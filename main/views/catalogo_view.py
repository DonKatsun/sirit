from django.shortcuts import render, redirect

def catalogo (request):
    categoria = request.GET.get('categoria_seleccionada')

    if categoria == 'conmutador':
        return render(request, 'conmutadores/conmutadores_list.html',)
    
    return render(request, 'catalogo.html', )