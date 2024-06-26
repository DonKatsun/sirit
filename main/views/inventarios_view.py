from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse 
from ..models import *
from django.contrib.auth.decorators import login_required
@login_required
def inventario(request):
    subcategoria = request.GET.get('subcategoriaSelec')
    year = request.GET.get('year')or ''
    dependencia = request.GET.get('dependenciaSelec')or ''
    serch = request.GET.get('serch')or ''
    descarga = request.GET.get('descarga')or ''
    secretaria = request.GET.get('secretariaSelec')or ''
    categoria = request.GET.get('categoria')or ''
    secretarias = Secretarias.objects.all().order_by('nombre_secretaria')
    dependencias = Dependencias.objects.all().order_by('nombre_dependencia')
    user_id = request.user.id
    usuario = (Usuarios.objects.get(usuario=user_id))
    rol=(usuario.id_rol.id)
    print(secretaria)
    if 'download' in request.GET:
        descarga='1'
    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)

    subcategoria_seleccionada = request.GET.get('subcategoriaSelec')
    if subcategoria_seleccionada:
        if subcategoria_seleccionada == "1092":
            return redirect(reverse('conmutadores_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1010":
            return redirect(reverse('energias_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1020":
            return redirect(reverse('almacenamientos_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1030":
            return redirect(reverse('equipos_personales_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1040":
            return redirect(reverse('equipos_servidores_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1050":
            return redirect(reverse('impresoras_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1060":
            return redirect(reverse('proyectores_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1080":
            return redirect(reverse('drones_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1090":
            return redirect(reverse('firewalls_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1091":
            return redirect(reverse('routers_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1110":
            return redirect(reverse('herramientas_desarrollo_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1120":
            return redirect(reverse('sistemas_informacion_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1130":
            return redirect(reverse('sistemas_informacion_movil_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1210":
            return redirect(reverse('enlaces_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1220":
            return redirect(reverse('enlaces_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1230":
            return redirect(reverse('sites_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1310":
            return redirect(reverse('usuarios_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1070":
            return redirect(reverse('equipo_telefonico_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
        if subcategoria_seleccionada == "1000" or subcategoria_seleccionada == "1100" or subcategoria_seleccionada == "1200" or subcategoria_seleccionada == "" or categoria=="200":
            return redirect(reverse('todo') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
        
    elif subcategoria_seleccionada == "1000" or subcategoria_seleccionada == "1100" or subcategoria_seleccionada == "1200" or subcategoria_seleccionada == "" or categoria=="200":
        return redirect(reverse('todo') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch+'&descarga='+descarga+'&secretariaSelec='+secretaria+'&categoria='+categoria)
    if rol != 1:
        return render(request, 'inventario.html', {
        'nav': "1",
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria')
    })
    else:
        return render(request, 'inventario.html', {
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria')
    })
    
def obtener_dependencias(request):
    secretaria_id = request.GET.get('secretaria')
    if not secretaria_id:
        return JsonResponse([], safe=False)
    # Filtrar dependencias por id_secretaria y ordenarlas alfabéticamente por nombre_dependencia
    dependencias = Dependencias.objects.filter(id_secretaria=secretaria_id).values('id', 'nombre_dependencia').order_by('nombre_dependencia')
    
    return JsonResponse(list(dependencias), safe=False)