from django.shortcuts import render, redirect
from ..models import *
from django.contrib.auth.decorators import login_required
@login_required
def clonar(request):
    if request.method == 'GET':
        year_origen = request.GET.get('year')
        year_destino = request.GET.get('year2')
        if year_origen and year_destino:
            #clonar_registros(Conmutadores, year_origen, year_destino)
            clonar_registros(Almacenamientos, year_origen, year_destino)
            clonar_registros(Conmutadores, year_origen, year_destino)
            clonar_registros(Drones, year_origen, year_destino)
            clonar_registros(Energias, year_origen, year_destino)
            clonar_registros(Enlaces, year_origen, year_destino)
            clonar_registros(EquipoTelefonico, year_origen, year_destino)
            clonar_registros(EquiposPersonales, year_origen, year_destino)
            clonar_registros(EquiposServidores, year_origen, year_destino)
            clonar_registros(Firewalls, year_origen, year_destino)
            clonar_registros(HerramientaDeDesarrollo, year_origen, year_destino)
            clonar_registros(Impresoras, year_origen, year_destino)
            clonar_registros(Proyectores, year_origen, year_destino)
            clonar_registros(Routers, year_origen, year_destino)
            clonar_registros(SistemaDeInformacionMovil, year_origen, year_destino)
            clonar_registros(SistemasInformacion, year_origen, year_destino)
            clonar_registros(Sites, year_origen, year_destino)


        return render(request, 'clonar.html')
    else:
        return render(request, 'clonar.html')

@login_required
def clonar_registros(modelo, year_origen, year_destino):
    registros_a_clonar = modelo.objects.filter(fecha__year=year_origen)
    
    for registro in registros_a_clonar:
        # Reemplazar el año de la fecha y establecer el mes y día a 1
        fecha_nueva = registro.fecha.replace(year=int(year_destino), month=1, day=1)
        
        # Crear un nuevo registro con la fecha actualizada
        nuevo_registro = modelo.objects.create(
            **{campo.name: getattr(registro, campo.name) for campo in registro._meta.fields if campo.name != 'id' and campo.name != 'fecha'},
        )
        nuevo_registro.fecha = fecha_nueva
        nuevo_registro.save()

