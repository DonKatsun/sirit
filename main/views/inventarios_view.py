from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse 
from ..models import *

def inventario(request):
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)

    subcategoria_seleccionada = request.GET.get('subcategoriaSelec')
    if subcategoria_seleccionada:
        if subcategoria_seleccionada == "1092":
            return redirect(reverse('conmutadores_list') + '?dependencia=2')
    return render(request, 'inventario.html', {
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria')
    })
def obtener_dependencias(request):
    secretaria_id = request.GET.get('secretaria')
    dependencias = Dependencias.objects.filter(id_secretaria=secretaria_id).values('id', 'nombre_dependencia')
    return JsonResponse(list(dependencias), safe=False)