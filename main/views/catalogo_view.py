from django.shortcuts import render, redirect
from .conmutadores_views import *
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
@login_required
def catalogo (request):
    categoria = request.GET.get('categoria_seleccionada')

    if categoria == 'sec':
        return redirect(reverse('secretarias_list'))
    
    if categoria == 'dep':
        return redirect(reverse('dependencias_list'))
    
    if categoria == 'marcas_almacenamiento':
        return redirect(reverse('almacenamientos_marcas_list'))
    
    if categoria == 'marcas_conmutadores':
        return redirect(reverse('conmutadores_marcas_list'))
    
    if categoria == 'drones_caracteristicas':
        return redirect(reverse('drones_caracteristicas_list'))
    
    if categoria == 'energia_marcas':
        return redirect(reverse('energia_marcas_list'))
    
    if categoria == 'ep_marcas':
        return redirect(reverse('equipos_personales_marcas_list'))
    
    if categoria == 'es_marcas':
        return redirect(reverse('equipos_servidores_marcas_list'))
    
    if categoria == 'es_procesadores':
        return redirect(reverse('equipos_servidores_procesadores_list'))

    if categoria == 'es_tipos':
        return redirect(reverse('equipos_servidores_tipos_list'))
    
    if categoria == 'f_marcas':
        return redirect(reverse('firewalls_marcas_list'))
    
    if categoria == 'i_marcas':
        return redirect(reverse('impresoras_marcas_list'))
    
    if categoria == 'p_marcas':
        return redirect(reverse('proyectores_marcas_list'))
    
    if categoria == 's_nombres':
        return redirect(reverse('sistemas_informacion_nombres_list'))
    
    if categoria == 'sm_nombres':
        return redirect(reverse('sistemas_informacion_movil_nombres_list'))
        
    return render(request, 'catalogo.html', )