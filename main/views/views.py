from django.http import JsonResponse
from django.shortcuts import render
from ..models import *
def obtener_dependencias(request):
    secretaria_id = request.GET.get('secretaria')
    dependencias = Dependencias.objects.filter(id_secretaria=secretaria_id).values('id', 'nombre_dependencia')
    return JsonResponse(list(dependencias), safe=False)