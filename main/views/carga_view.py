from django.shortcuts import render, redirect
from .conmutadores_views import *
from django.urls import reverse 
import pandas as pd


def carga (request):
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    archivo_excel = request.FILES['ex']
    print(archivo_excel)

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)

    if request.method == 'POST' and archivo_excel:
        
        try:
            df = pd.read_excel(archivo_excel)
        except Exception as e:
            return render(request, 'error.html', {'mensaje': f"Error al leer el archivo Excel: {str(e)}"})
        
        # Obtener las cabeceras y los datos
        cabeceras = df.columns.tolist()
        datos = df.values.tolist()
        

        return render(request, 'carga.html', {
            'cabeceras': cabeceras,
            'datos': datos,
            'secretarias': secretarias,
            'dependencias': dependencias,
            'selected_secretaria': request.GET.get('secretaria')
            })

    return render(request,"carga.html", {
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria')})