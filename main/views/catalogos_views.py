from django.shortcuts import render, redirect
from ..models import *
from ..forms import *

from django.db.models import Q


from django.shortcuts import render, redirect
from ..models import ConmutadoresMarcas
from ..forms import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from django.apps import apps
import openpyxl
from django.http import HttpResponse

def generate_excel(model_name, queryset):
    model = apps.get_model(app_label='main', model_name=model_name)
    wb = openpyxl.Workbook()
    ws = wb.active

    headers = [field.name for field in model._meta.fields]
    ws.append(headers)

    for obj in queryset:
        row = []
        for field in headers:
            value = getattr(obj, field)
            if isinstance(value, models.Model):
                # Obtén el campo en la posición 2
                related_model_fields = [f.name for f in value._meta.fields]
                if len(related_model_fields) >= 2:
                    value = getattr(value, related_model_fields[1])
                else:
                    value = str(value)  # En caso de que no haya suficientes campos, usa la representación por defecto
            row.append(value)
        ws.append(row)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={model_name}.xlsx'
    wb.save(response)
    return response
########################
# CRUD Operations for ConmutadoresMarcas Model
########################
def usu(request):
    user_id = request.user.id
    usuario = (Usuarios.objects.get(usuario=user_id))
    rol=(usuario.id_rol.id)
    return rol
@login_required
def conmutadores_marcas_list(request):
    rol = usu(request)
    conmutadores_marcas_list = ConmutadoresMarcas.objects.all()
    paginator = Paginator(conmutadores_marcas_list, 10)  # Muestra 10 marcas de conmutadores por página

    page_number = request.GET.get('page')
    try:
        conmutadores_marcas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        conmutadores_marcas = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        conmutadores_marcas = paginator.page(paginator.num_pages)

    if rol != 1:
        return render(request, 'conmutadores_marcas/conmutadores_marcas_list.html', {'conmutadores_marcas': conmutadores_marcas,'nav': str(rol),})
    return render(request, 'conmutadores_marcas/conmutadores_marcas_list.html', {'conmutadores_marcas': conmutadores_marcas})

@login_required
def conmutadores_marca_detail(request, pk):
    conmutador_marca = ConmutadoresMarcas.objects.get(pk=pk)
    return render(request, 'conmutadores_marcas/conmutadores_marca_detail.html', {'conmutador_marca': conmutador_marca})

@login_required
def conmutadores_marca_create(request):
    if request.method == 'POST':
        form = ConmutadorMarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conmutadores_marcas_list')
    else:
        form = ConmutadorMarcaForm()
    return render(request, 'conmutadores_marcas/conmutadores_marca_form.html', {'form': form})

@login_required
def conmutadores_marca_update(request, pk):
    conmutador_marca = ConmutadoresMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = ConmutadorMarcaForm(request.POST, instance=conmutador_marca)
        if form.is_valid():
            form.save()
            return redirect('conmutadores_marcas_list')
    else:
        form = ConmutadorMarcaForm(instance=conmutador_marca)
    return render(request, 'conmutadores_marcas/conmutadores_marca_form.html', {'form': form})

@login_required
def conmutadores_marca_delete(request, pk):
    conmutador_marca = ConmutadoresMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        conmutador_marca.delete()
        return redirect('conmutadores_marcas_list')
    return render(request, 'conmutadores_marcas/conmutadores_marca_confirm_delete.html', {'conmutador_marca': conmutador_marca})

########################
# End of CRUD Operations for ConmutadoresMarcas Model
########################

########################
# CRUD Operations for Conmutadores Puertos Model
########################

@login_required
def conmutadores_puertos_list(request):
    rol = usu(request)
    conmutadores_puertos_list = ConmutadoresPuertos.objects.all()
    paginator = Paginator(conmutadores_puertos_list, 10)  # Muestra 10 marcas de conmutadores por página

    page_number = request.GET.get('page')
    try:
        conmutadores_puertos = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        conmutadores_puertos = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        conmutadores_puertos = paginator.page(paginator.num_pages)

    if rol != 1:
        return render(request, 'conmutadores_puertos/conmutadores_puertos_list.html', {'conmutadores_puertos': conmutadores_puertos,'rol': rol})
    return render(request, 'conmutadores_puertos/conmutadores_puertos_list.html', {'conmutadores_puertos': conmutadores_puertos})

@login_required
def conmutadores_puerto_detail(request, pk):
    conmutador_puerto = ConmutadoresPuertos.objects.get(pk=pk)
    return render(request, 'conmutadores_puertos/conmutadores_puerto_detail.html', {'conmutador_puerto': conmutador_puerto})

@login_required
def conmutadores_puerto_create(request):
    if request.method == 'POST':
        form = ConmutadorPuertoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conmutadores_puertos_list')
    else:
        form = ConmutadorPuertoForm()
    return render(request, 'conmutadores_puertos/conmutadores_puerto_form.html', {'form': form})

@login_required
def conmutadores_puerto_update(request, pk):
    conmutador_puerto = ConmutadoresPuertos.objects.get(pk=pk)
    if request.method == 'POST':
        form = ConmutadorPuertoForm(request.POST, instance=conmutador_puerto)
        if form.is_valid():
            form.save()
            return redirect('conmutadores_puertos_list')
    else:
        form = ConmutadorPuertoForm(instance=conmutador_puerto)
    return render(request, 'conmutadores_puertos/conmutadores_puerto_form.html', {'form': form})

@login_required
def conmutadores_puerto_delete(request, pk):
    conmutador_puerto = ConmutadoresPuertos.objects.get(pk=pk)
    if request.method == 'POST':
        conmutador_puerto.delete()
        return redirect('conmutadores_puertos_list')
    return render(request, 'conmutadores_puertos/conmutadores_puerto_confirm_delete.html', {'conmutador_puerto': conmutador_puerto})

########################
# End of CRUD Operations for Conmutadores Puertos Model
########################

########################
# CRUD Operations for Almacenamientos Model
########################


@login_required
def almacenamientos_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    #almacenamientos_list = Almacenamientos.objects.all()
    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        if secretaria:
            almacenamientos_list = Almacenamientos.objects.filter(id_dependencia__id_secretaria=secretaria,fecha__year=year)
        
        if dependencia:
            almacenamientos_list = Almacenamientos.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            almacenamientos_list = Almacenamientos.objects.filter(fecha__year=year)
    else:
        almacenamientos_list = Almacenamientos.objects.all()
    if secretaria:
        almacenamientos_list = almacenamientos_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        almacenamientos_list = almacenamientos_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('almacenamientos', almacenamientos_list)
    paginator = Paginator(almacenamientos_list, 10)  # Muestra 10 drones por página

    page_number = request.GET.get('page')
    try:
        almacenamientos = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        almacenamientos = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        almacenamientos = paginator.page(paginator.num_pages)
    if rol != 1:
        return render(request, 'almacenamientos/almacenamientos_list.html', {
        'almacenamientos': almacenamientos,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Almacenamiento',
        'clave': '1020',
        'nav': rol})
    return render(request, 'almacenamientos/almacenamientos_list.html', {
        'almacenamientos': almacenamientos,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Almacenamiento',
        'clave': '1020',
        })
    
@login_required
def almacenamiento_detail(request, pk):
    almacenamiento = Almacenamientos.objects.get(pk=pk)
    return render(request, 'almacenamientos/almacenamiento_detail.html', {'almacenamiento': almacenamiento})

@login_required
def almacenamiento_create(request):
    if request.method == 'POST':
        form = AlmacenamientosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('almacenamientos_list')
    else:
        form = AlmacenamientosForm()
    return render(request, 'almacenamientos/almacenamiento_form.html', {'form': form})

@login_required
def almacenamiento_update(request, pk):
    almacenamiento = Almacenamientos.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlmacenamientosForm(request.POST, instance=almacenamiento)
        if form.is_valid():
            form.save()
            return redirect('almacenamientos_list')
    else:
        form = AlmacenamientosForm(instance=almacenamiento)
    return render(request, 'almacenamientos/almacenamiento_form.html', {'form': form})

@login_required
def almacenamiento_delete(request, pk):
    almacenamiento = Almacenamientos.objects.get(pk=pk)
    if request.method == 'POST':
        almacenamiento.delete()
        return redirect('almacenamientos_list')
    return render(request, 'almacenamientos/almacenamiento_confirm_delete.html', {'almacenamiento': almacenamiento})

########################
# End of CRUD Operations for Almacenamientos Model
########################

########################
# CRUD Operations for Almacenamientos Marcas Model
########################


@login_required
def almacenamientos_marcas_list(request):
    rol = usu(request)
    almacenamientos_marcas_list = AlmacenamientoMarcas.objects.all()
    paginator = Paginator(almacenamientos_marcas_list, 10)  # Muestra 10 drones por página

    page_number = request.GET.get('page')
    try:
        almacenamientos_marcas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        almacenamientos_marcas = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        almacenamientos_marcas = paginator.page(paginator.num_pages)

    return render(request, 'almacenamientos_marcas/almacenamientos_marcas_list.html', {'almacenamientos_marcas': almacenamientos_marcas})
    
@login_required
def almacenamiento_marca_detail(request, pk):
    almacenamiento_marca = AlmacenamientoMarcas.objects.get(pk=pk)
    return render(request, 'almacenamientos_marcas/almacenamiento_marca_detail.html', {'almacenamiento_marca': almacenamiento_marca})

@login_required
def almacenamiento_marca_create(request):
    if request.method == 'POST':
        form = AlmacenamientoMarcasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('almacenamientos_marcas_list')
    else:
        form = AlmacenamientoMarcasForm()
    return render(request, 'almacenamientos_marcas/almacenamiento_marca_form.html', {'form': form})

@login_required
def almacenamiento_marca_update(request, pk):
    almacenamiento_marca = AlmacenamientoMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlmacenamientoMarcasForm(request.POST, instance=almacenamiento_marca)
        if form.is_valid():
            form.save()
            return redirect('almacenamientos_marcas_list')
    else:
        form = AlmacenamientoMarcasForm(instance=almacenamiento_marca)
    return render(request, 'almacenamientos_marcas/almacenamiento_marca_form.html', {'form': form})

@login_required
def almacenamiento_marca_delete(request, pk):
    almacenamiento_marca = AlmacenamientoMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        almacenamiento_marca.delete()
        return redirect('almacenamientos_marcas_list')
    return render(request, 'almacenamientos_marcas/almacenamiento_marca_confirm_delete.html', {'almacenamiento_marca': almacenamiento_marca})

########################
# End of CRUD Operations for Almacenamientos Marcas Model
########################
########################
# CRUD Operations for Dependencias Model
########################
        
@login_required
def dependencias_list(request):
    rol = usu(request)
    dependencias = Dependencias.objects.all()
    return render(request, 'dependencias/dependencias_list.html', {'dependencias': dependencias})

@login_required
def dependencia_detail(request, pk):
    dependencia = Dependencias.objects.get(pk=pk)
    return render(request, 'dependencias/dependencia_detail.html', {'dependencia': dependencia})

@login_required
def dependencia_create(request):
    if request.method == 'POST':
        form = DependenciasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dependencias_list')
    else:
        form = DependenciasForms()
    return render(request, 'dependencias/dependencia_form.html', {'form': form})

@login_required
def dependencia_update(request, pk):
    dependencia = Dependencias.objects.get(pk=pk)
    if request.method == 'POST':
        form = DependenciasForms(request.POST, instance=dependencia)
        if form.is_valid():
            form.save()
            return redirect('dependencias_list')
    else:
        form = DependenciasForms(instance=dependencia)
    return render(request, 'dependencias/dependencia_form.html', {'form': form})

@login_required
def dependencia_delete(request, pk):
    dependencia = Dependencias.objects.get(pk=pk)
    if request.method == 'POST':
        dependencia.delete()
        return redirect('dependencias_list')
    return render(request, 'dependencias/dependencia_confirm_delete.html', {'dependencia': dependencia})

########################
# End of CRUD Operations for Dependencias Model
########################

########################
# CRUD Operations for Drones Model
########################

@login_required
def drones_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    #drones_list = Drones.objects.all()
    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            drones_list = Drones.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            drones_list = Drones.objects.filter(fecha__year=year)
    else:
        drones_list = Drones.objects.all()
    if secretaria:
        drones_list = drones_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        drones_list = drones_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('drones', drones_list)

    paginator = Paginator(drones_list, 10)  # Muestra 10 drones por página

    page_number = request.GET.get('page')
    try:
        drones = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        drones = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        drones = paginator.page(paginator.num_pages)
    if rol != 1:
        return render(request, 'drones/drones_list.html', {'drones': drones,'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Dron',
        'clave': '1080','nav':rol})
    
    return render(request, 'drones/drones_list.html', {'drones': drones,'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Dron',
        'clave': '1080',
        })


@login_required
def drone_detail(request, pk):
    drone = Drones.objects.get(pk=pk)
    return render(request, 'drones/drone_detail.html', {'drone': drone})

@login_required
def drone_create(request):
    if request.method == 'POST':
        form = DronesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drones_list')
    else:
        form = DronesForms()
    return render(request, 'drones/drone_form.html', {'form': form})

@login_required
def drone_update(request, pk):
    drone = Drones.objects.get(pk=pk)
    if request.method == 'POST':
        form = DronesForms(request.POST, instance=drone)
        if form.is_valid():
            form.save()
            return redirect('drones_list')
    else:
        form = DronesForms(instance=drone)
    return render(request, 'drones/drone_form.html', {'form': form})

@login_required
def drone_delete(request, pk):
    drone = Drones.objects.get(pk=pk)
    if request.method == 'POST':
        drone.delete()
        return redirect('drones_list')
    return render(request, 'drones/drone_confirm_delete.html', {'drone': drone})

########################
# End of CRUD Operations for Drones Model
########################

########################
# CRUD Operations for DronesCaracteristicas Model
########################

@login_required
def drones_caracteristicas_list(request):
    rol = usu(request)
    drones_caracteristicas_list = DronesCaracteristicas.objects.all()
    paginator = Paginator(drones_caracteristicas_list, 10)  # Muestra 10 características de drones por página

    page_number = request.GET.get('page')
    try:
        drones_caracteristicas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        drones_caracteristicas = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        drones_caracteristicas = paginator.page(paginator.num_pages)

    return render(request, 'drones_caracteristicas/drones_caracteristicas_list.html', {'drones_caracteristicas': drones_caracteristicas})

@login_required
def drones_caracteristica_detail(request, pk):
    drone_caracteristica = DronesCaracteristicas.objects.get(pk=pk)
    return render(request, 'drones_caracteristicas/drones_caracteristica_detail.html', {'drone_caracteristica': drone_caracteristica})

@login_required
def drones_caracteristica_create(request):
    if request.method == 'POST':
        form = DronesCaracteristicasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drones_caracteristicas_list')
    else:
        form = DronesCaracteristicasForms()
    return render(request, 'drones_caracteristicas/drones_caracteristica_form.html', {'form': form})

@login_required
def drones_caracteristica_update(request, pk):
    drone_caracteristica = DronesCaracteristicas.objects.get(pk=pk)
    if request.method == 'POST':
        form = DronesCaracteristicasForms(request.POST, instance=drone_caracteristica)
        if form.is_valid():
            form.save()
            return redirect('drones_caracteristicas_list')
    else:
        form = DronesCaracteristicasForms(instance=drone_caracteristica)
    return render(request, 'drones_caracteristicas/drones_caracteristica_form.html', {'form': form})

@login_required
def drones_caracteristica_delete(request, pk):
    drone_caracteristica = DronesCaracteristicas.objects.get(pk=pk)
    if request.method == 'POST':
        drone_caracteristica.delete()
        return redirect('drones_caracteristicas_list')
    return render(request, 'drones_caracteristicas/drones_caracteristica_confirm_delete.html', {'drone_caracteristica': drone_caracteristica})

########################
# End of CRUD Operations for DronesAsignacion Model
########################

@login_required
def drones_asignaciones_list(request):
    rol = usu(request)
    drones_asignaciones_list = DronesAsignacionCaracteristicas.objects.all()
    paginator = Paginator(drones_asignaciones_list, 10)  # Muestra 10 drones por página

    page_number = request.GET.get('page')
    try:
        drones_asignaciones = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        drones_asignaciones = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        drones_asignaciones = paginator.page(paginator.num_pages)

    return render(request, 'drones_asignacion/drones_asignaciones_list.html', {'drones_asignaciones': drones_asignaciones})

@login_required
def drone_asignacion_detail(request, pk):
    drone_asignacion = DronesAsignacionCaracteristicas.objects.get(pk=pk)
    return render(request, 'drones_asignacion/drone_asignacion_detail.html', {'drone_asignacion': drone_asignacion})

@login_required
def drone_asignacion_create(request):
    if request.method == 'POST':
        form = DronesAsignacionCaracteristicasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drones_asignaciones_list')
    else:
        form = DronesAsignacionCaracteristicasForms()
    return render(request, 'drones_asignacion/drone_asignacion_form.html', {'form': form})

@login_required
def drone_asignacion_update(request, pk):
    drone_asignacion = DronesAsignacionCaracteristicas.objects.get(pk=pk)
    if request.method == 'POST':
        form = DronesAsignacionCaracteristicasForms(request.POST, instance=drone_asignacion)
        if form.is_valid():
            form.save()
            return redirect('drones_asignaciones_list')
    else:
        form = DronesAsignacionCaracteristicasForms(instance=drone_asignacion)
    return render(request, 'drones_asignacion/drone_asignacion_form.html', {'form': form})

@login_required
def drone_asignacion_delete(request, pk):
    drone_asignacion = DronesAsignacionCaracteristicas.objects.get(pk=pk)
    if request.method == 'POST':
        drone_asignacion.delete()
        return redirect('drones_list')
    return render(request, 'drones_asignacion/drone_asignacion_confirm_delete.html', {'drone_asignacion': drone_asignacion})

########################
# End of CRUD Operations for Drones asignacion |Model
########################

########################
# CRUD Operations for EnergiaMarcas Model
########################

@login_required
def energia_marcas_list(request):
    rol = usu(request)
    energia_marcas_list = EnergiaMarcas.objects.all()
    paginator = Paginator(energia_marcas_list, 10)  # Muestra 10 marcas de energía por página

    page_number = request.GET.get('page')
    try:
        energia_marcas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        energia_marcas = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        energia_marcas = paginator.page(paginator.num_pages)

    return render(request, 'energia_marcas/energia_marcas_list.html', {'energia_marcas': energia_marcas})


@login_required
def energia_marca_create(request):
    if request.method == 'POST':
        form = EnergiaMarcasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('energia_marcas_list')
    else:
        form = EnergiaMarcasForms()
    return render(request, 'energia_marcas/energia_marca_form.html', {'form': form})

@login_required
def energia_marca_update(request, pk):
    energia_marca = EnergiaMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = EnergiaMarcasForms(request.POST, instance=energia_marca)
        if form.is_valid():
            form.save()
            return redirect('energia_marcas_list')
    else:
        form = EnergiaMarcasForms(instance=energia_marca)
    return render(request, 'energia_marcas/energia_marca_form.html', {'form': form})


@login_required
def energia_marca_delete(request, pk):
    energia_marca = EnergiaMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        energia_marca.delete()
        return redirect('energia_marcas_list')
    return render(request, 'energia_marcas/energia_marca_confirm_delete.html', {'energia_marca': energia_marca})

########################
# End of CRUD Operations for EnergiaMarcas Model
########################

########################
# CRUD Operations for Energias Model
########################

@login_required
def energias_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    energias_list = Energias.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            energias_list = Energias.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            energias_list = Energias.objects.filter(fecha__year=year)
    else:
        energias_list = Energias.objects.all()
    
    if secretaria:
        energias_list = energias_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        energias_list = energias_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('energias', energias_list)
    paginator = Paginator(energias_list, 10)  # 10 registros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if rol != 1:
        return render(request, 'energia/energias_list.html', {
        'page_obj': page_obj,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Energia',
        'clave': '1010',
        'nav':rol
        })
    return render(request, 'energia/energias_list.html', {
        'page_obj': page_obj,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Energia',
        'clave': '1010',
        })

@login_required
def energia_detail(request, pk):
    energia = Energias.objects.get(pk=pk)
    return render(request, 'energia/energia_detail.html', {
        'energia': energia,
        
        })

@login_required
def energia_create(request):
    if request.method == 'POST':
        form = EnergiasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('energias_list')
    else:
        form = EnergiasForms()
    return render(request, 'energia/energia_form.html', {'form': form})

@login_required
def energia_update(request, pk):
    energia = Energias.objects.get(pk=pk)
    if request.method == 'POST':
        form = EnergiasForms(request.POST, instance=energia)
        if form.is_valid():
            form.save()
            return redirect('energias_list')
    else:
        form = EnergiasForms(instance=energia)
    return render(request, 'energia/energia_form.html', {'form': form})

@login_required
def energia_delete(request, pk):
    energia = Energias.objects.get(pk=pk)
    if request.method == 'POST':
        energia.delete()
        return redirect('energias_list')
    return render(request, 'energia/energia_confirm_delete.html', {'energia': energia})

########################
# End of CRUD Operations for Energias Model
########################

########################
# CRUD Operations for Enlaces Model
########################

@login_required
def enlaces_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    enlaces_list = Enlaces.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            enlaces_list = Enlaces.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            enlaces_list = Enlaces.objects.filter(fecha__year=year)
    else:
        enlaces_list = Enlaces.objects.all()
    
    if secretaria:
        enlaces_list = enlaces_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        enlaces_list = enlaces_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('enlaces', enlaces_list)
    paginator = Paginator(enlaces_list, 10)  # Muestra 10 enlaces por página

    page_number = request.GET.get('page')
    try:
        enlaces = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        enlaces = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        enlaces = paginator.page(paginator.num_pages)
    if rol != 1:
        return render(request, 'enlaces/enlaces_list.html', {
        'enlaces': enlaces,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Enlaces',
        'clave': '1210',
        'nav':rol
        })
    return render(request, 'enlaces/enlaces_list.html', {
        'enlaces': enlaces,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Enlaces',
        })


@login_required
def enlace_detail(request, pk):
    enlace = Enlaces.objects.get(pk=pk)
    return render(request, 'enlaces/enlace_detail.html', {'enlace': enlace})

@login_required
def enlace_create(request):
    if request.method == 'POST':
        form = EnlacesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enlaces_list')
    else:
        form = EnlacesForms()
    return render(request, 'enlaces/enlace_form.html', {'form': form})

@login_required
def enlace_update(request, pk):
    enlace = Enlaces.objects.get(pk=pk)
    if request.method == 'POST':
        form = EnlacesForms(request.POST, instance=enlace)
        if form.is_valid():
            form.save()
            return redirect('enlaces_list')
    else:
        form = EnlacesForms(instance=enlace)
    return render(request, 'enlaces/enlace_form.html', {'form': form})

@login_required
def enlace_delete(request, pk):
    enlace = Enlaces.objects.get(pk=pk)
    if request.method == 'POST':
        enlace.delete()
        return redirect('enlaces_list')
    return render(request, 'enlaces/enlace_confirm_delete.html', {'enlace': enlace})

########################
# End of CRUD Operations for Enlaces Model
########################

########################
# CRUD Operations for EnlacesTipos Model
########################

@login_required
def enlaces_tipos_list(request):
    rol = usu(request)
    enlaces_tipos_list = EnlacesTipos.objects.all()
    paginator = Paginator(enlaces_tipos_list, 10)  # Muestra 10 tipos de enlaces por página

    page_number = request.GET.get('page')
    try:
        enlaces_tipos = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        enlaces_tipos = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        enlaces_tipos = paginator.page(paginator.num_pages)

    return render(request, 'enlaces/enlaces_tipos_list.html', {'enlaces_tipos': enlaces_tipos})

@login_required
def enlace_tipo_detail(request, pk):
    enlace_tipo = EnlacesTipos.objects.get(pk=pk)
    return render(request, 'enlaces/enlace_tipo_detail.html', {'enlace_tipo': enlace_tipo})

@login_required
def enlace_tipo_create(request):
    if request.method == 'POST':
        form = EnlacesTiposForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enlaces_tipos_list')
    else:
        form = EnlacesTiposForms()
    return render(request, 'enlaces/enlace_tipo_form.html', {'form': form})

@login_required
def enlace_tipo_update(request, pk):
    enlace_tipo = EnlacesTipos.objects.get(pk=pk)
    if request.method == 'POST':
        form = EnlacesTiposForms(request.POST, instance=enlace_tipo)
        if form.is_valid():
            form.save()
            return redirect('enlaces_tipos_list')
    else:
        form = EnlacesTiposForms(instance=enlace_tipo)
    return render(request, 'enlaces/enlace_tipo_form.html', {'form': form})

@login_required
def enlace_tipo_delete(request, pk):
    enlace_tipo = EnlacesTipos.objects.get(pk=pk)
    if request.method == 'POST':
        enlace_tipo.delete()
        return redirect('enlaces_tipos_list')
    return render(request, 'enlaces/enlace_tipo_confirm_delete.html', {'enlace_tipo': enlace_tipo})

########################
# End of CRUD Operations for EnlacesTipos Model
########################

########################
# CRUD Operations for EquipoTelefonico Model
########################

@login_required
def equipo_telefonico_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    #equipo_telefonico_list = EquipoTelefonico.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            equipo_telefonico_list = EquipoTelefonico.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            equipo_telefonico_list = EquipoTelefonico.objects.filter(fecha__year=year)
    else:
        equipo_telefonico_list = EquipoTelefonico.objects.all()

    if secretaria:
        equipo_telefonico_list = equipo_telefonico_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        equipo_telefonico_list = equipo_telefonico_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('equipotelefonico', equipo_telefonico_list)
    paginator = Paginator(equipo_telefonico_list, 10)  # Muestra 10 equipos telefónicos por página

    page_number = request.GET.get('page')
    try:
        equipos_telefonicos = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        equipos_telefonicos = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        equipos_telefonicos = paginator.page(paginator.num_pages)

    if rol != 1:
        return render(request, 'equipos/equipo_telefonico_list.html', {
        'equipos_telefonicos': equipos_telefonicos,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Equipo Telefonico',
        'clave': '1070',
        'nav':rol
        })
    return render(request, 'equipos/equipo_telefonico_list.html', {
        'equipos_telefonicos': equipos_telefonicos,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Equipo Telefonico',
        'clave': '1070',
        })

@login_required
def equipo_telefonico_detail(request, pk):
    equipo = EquipoTelefonico.objects.get(pk=pk)
    return render(request, 'equipos/equipo_telefonico_detail.html', {'equipo': equipo})

@login_required
def equipo_telefonico_create(request):
    if request.method == 'POST':
        form = EquipoTelefonicoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipo_telefonico_list')
    else:
        form = EquipoTelefonicoForms()
    return render(request, 'equipos/equipo_telefonico_form.html', {'form': form})

@login_required
def equipo_telefonico_update(request, pk):
    equipo = EquipoTelefonico.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquipoTelefonicoForms(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('equipo_telefonico_list')
    else:
        form = EquipoTelefonicoForms(instance=equipo)
    return render(request, 'equipos/equipo_telefonico_form.html', {'form': form})

@login_required
def equipo_telefonico_delete(request, pk):
    equipo = EquipoTelefonico.objects.get(pk=pk)
    if request.method == 'POST':
        equipo.delete()
        return redirect('equipo_telefonico_list')
    return render(request, 'equipos/equipo_telefonico_confirm_delete.html', {'equipo': equipo})

########################
# End of CRUD Operations for EquipoTelefonico Model
########################

########################
# CRUD Operations for EquiposPersonales Model
########################

@login_required
def equipos_personales_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    #equipos_personales_list = EquiposPersonales.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            equipos_personales_list = EquiposPersonales.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            equipos_personales_list = EquiposPersonales.objects.filter(fecha__year=year)
    else:
        equipos_personales_list = EquiposPersonales.objects.all()

    if secretaria:
        equipos_personales_list = equipos_personales_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        equipos_personales_list = equipos_personales_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('EquiposPersonales', equipos_personales_list)
    paginator = Paginator(equipos_personales_list, 10)  # Muestra 10 equipos personales por página

    page_number = request.GET.get('page')
    try:
        equipos_personales = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        equipos_personales = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        equipos_personales = paginator.page(paginator.num_pages)

    if rol != 1:
        return render(request, 'equiposp/equipos_personales_list.html', {
        'equipos_personales': equipos_personales,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Equipos personales',
        'clave': '1030',
        'nav':rol
        })
    return render(request, 'equiposp/equipos_personales_list.html', {
        'equipos_personales': equipos_personales,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Equipos personales',
        'clave': '1030',
        })

@login_required
def equipo_personal_detail(request, pk):
    equipo_personal = EquiposPersonales.objects.get(pk=pk)
    return render(request, 'equiposp/equipo_personal_detail.html', {'equipo_personal': equipo_personal})

@login_required
def equipo_personal_create(request):
    if request.method == 'POST':
        form = EquiposPersonalesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_personales_list')
    else:
        form = EquiposPersonalesForms()
    return render(request, 'equiposp/equipo_personal_form.html', {'form': form})

@login_required
def equipo_personal_update(request, pk):
    equipo_personal = EquiposPersonales.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposPersonalesForms(request.POST, instance=equipo_personal)
        if form.is_valid():
            form.save()
            return redirect('equipos_personales_list')
    else:
        form = EquiposPersonalesForms(instance=equipo_personal)
    return render(request, 'equiposp/equipo_personal_form.html', {'form': form})

@login_required
def equipo_personal_delete(request, pk):
    equipo_personal = EquiposPersonales.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_personal.delete()
        return redirect('equipos_personales_list')
    return render(request, 'equiposp/equipo_personal_confirm_delete.html', {'equipo_personal': equipo_personal})

########################
# End of CRUD Operations for EquiposPersonales Model
########################

########################
# CRUD Operations for EquiposPersonalesMarcas Model
########################

@login_required
def equipos_personales_marcas_list(request):
    rol = usu(request)
    equipos_personales_marcas_list = EquiposPersonalesMarcas.objects.all()
    paginator = Paginator(equipos_personales_marcas_list, 10)  # Muestra 10 equipos personales marcas por página

    page_number = request.GET.get('page')
    try:
        equipos_personales_marcas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        equipos_personales_marcas = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        equipos_personales_marcas = paginator.page(paginator.num_pages)

    return render(request, 'equipos_marcas/equipos_personales_marcas_list.html', {'equipos_personales_marcas': equipos_personales_marcas})

@login_required
def equipo_personal_marca_detail(request, pk):
    equipo_personal_marca = EquiposPersonalesMarcas.objects.get(pk=pk)
    return render(request, 'equipos_marcas/equipo_personal_marca_detail.html', {'equipo_personal_marca': equipo_personal_marca})

@login_required
def equipo_personal_marca_create(request):
    if request.method == 'POST':
        form = EquiposPersonalesMarcasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_personales_marcas_list')
    else:
        form = EquiposPersonalesMarcasForms()
    return render(request, 'equipos_marcas/equipo_personal_marca_form.html', {'form': form})

@login_required
def equipo_personal_marca_update(request, pk):
    equipo_personal_marca = EquiposPersonalesMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposPersonalesMarcasForms(request.POST, instance=equipo_personal_marca)
        if form.is_valid():
            form.save()
            return redirect('equipos_personales_marcas_list')
    else:
        form = EquiposPersonalesMarcasForms(instance=equipo_personal_marca)
    return render(request, 'equipos_marcas/equipo_personal_marca_form.html', {'form': form})

@login_required
def equipo_personal_marca_delete(request, pk):
    equipo_personal_marca = EquiposPersonalesMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_personal_marca.delete()
        return redirect('equipos_personales_marcas_list')
    return render(request, 'equipos_marcas/equipo_personal_marca_confirm_delete.html', {'equipo_personal_marca': equipo_personal_marca})

########################
# End of CRUD Operations for EquiposPersonalesMarcas Model
########################      

########################
# CRUD Operations for EquiposPersonalesPuertos Model
########################

@login_required
def equipos_personales_puertos_list(request):
    rol = usu(request)
    equipos_personales_puertos_list = EquiposPersonalesPuertos.objects.all()
    paginator = Paginator(equipos_personales_puertos_list, 10)  # Muestra 10 equipos personales marcas por página

    page_number = request.GET.get('page')
    try:
        equipos_personales_puertos = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        equipos_personales_puertos = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        equipos_personales_puertos = paginator.page(paginator.num_pages)

    return render(request, 'equipos_puertos/equipos_personales_puertos_list.html', {'equipos_personales_puertos': equipos_personales_puertos})

@login_required
def equipo_personal_puerto_detail(request, pk):
    equipo_personal_puerto = EquiposPersonalesPuertos.objects.get(pk=pk)
    return render(request, 'equipos_puertos/equipo_personal_puerto_detail.html', {'equipo_personal_puerto': equipo_personal_puerto})

@login_required
def equipo_personal_puerto_create(request):
    if request.method == 'POST':
        form = EquiposPersonalesPuertosForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_personales_puertos_list')
    else:
        form = EquiposPersonalesPuertosForms()
    return render(request, 'equipos_puertos/equipo_personal_puerto_form.html', {'form': form})

@login_required
def equipo_personal_puerto_update(request, pk):
    equipo_personal_puerto = EquiposPersonalesPuertos.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposPersonalesPuertosForms(request.POST, instance=equipo_personal_puerto)
        if form.is_valid():
            form.save()
            return redirect('equipos_personales_puertos_list')
    else:
        form = EquiposPersonalesPuertosForms(instance=equipo_personal_puerto)
    return render(request, 'equipos_puertos/equipo_personal_puerto_form.html', {'form': form})

@login_required
def equipo_personal_puerto_delete(request, pk):
    equipo_personal_puerto = EquiposPersonalesPuertos.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_personal_puerto.delete()
        return redirect('equipos_personales_puertos_list')
    return render(request, 'equipos_puertos/equipo_personal_puerto_confirm_delete.html', {'equipo_personal_puerto': equipo_personal_puerto})

########################
# End of CRUD Operations for EquiposPersonalesMarcas Model
########################      

########################
# CRUD Operations for EquiposPersonalesPuertos Model
########################

@login_required
def equipos_personales_tipopuertos_list(request):
    rol = usu(request)
    equipos_personales_tipopuertos_list = EquiposPersonalesTipopuertos.objects.all()
    paginator = Paginator(equipos_personales_tipopuertos_list, 10)  # Muestra 10 equipos personales marcas por página

    page_number = request.GET.get('page')
    try:
        equipos_personales_tipopuertos = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        equipos_personales_tipopuertos = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        equipos_personales_tipopuertos = paginator.page(paginator.num_pages)

    return render(request, 'equipos_puertos/equipos_personales_tipopuertos_list.html', {'equipos_personales_tipopuertos': equipos_personales_tipopuertos})

@login_required
def equipo_personal_tipopuerto_detail(request, pk):
    equipo_personal_tipopuerto = EquiposPersonalesTipopuertos.objects.get(pk=pk)
    return render(request, 'equipos_puertos/equipo_personal_tipopuerto_detail.html', {'equipo_personal_tipopuerto': equipo_personal_tipopuerto})

@login_required
def equipo_personal_tipopuerto_create(request):
    if request.method == 'POST':
        form = EquiposPersonalesTipoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_personales_tipopuertos_list')
    else:
        form = EquiposPersonalesTipoForms()
    return render(request, 'equipos_puertos/equipo_personal_tipopuerto_form.html', {'form': form})

@login_required
def equipo_personal_tipopuerto_update(request, pk):
    equipo_personal_tipopuerto = EquiposPersonalesTipopuertos.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposPersonalesTipoForms(request.POST, instance=equipo_personal_tipopuerto)
        if form.is_valid():
            form.save()
            return redirect('equipos_personales_tipopuertos_list')
    else:
        form = EquiposPersonalesTipoForms(instance=equipo_personal_tipopuerto)
    return render(request, 'equipos_puertos/equipo_personal_tipopuerto_form.html', {'form': form})

@login_required
def equipo_personal_tipopuerto_delete(request, pk):
    equipo_personal_tipopuerto = EquiposPersonalesTipopuertos.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_personal_tipopuerto.delete()
        return redirect('equipos_personales_tipopuertos_list')
    return render(request, 'equipos_puertos/equipo_personal_tipopuerto_confirm_delete.html', {'equipo_personal_tipopuerto': equipo_personal_tipopuerto})

########################
# End of CRUD Operations for EquiposPersonalesMarcas Model
########################

########################
# CRUD Operations for EquiposServidores Model
########################

@login_required
def equipos_servidores_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    #equipos_servidores_list = EquiposServidores.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            equipos_servidores_list = EquiposServidores.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            equipos_servidores_list = EquiposServidores.objects.filter(fecha__year=year)
    else:
        equipos_servidores_list = EquiposServidores.objects.all()
    if secretaria:
        equipos_servidores_list = equipos_servidores_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        equipos_servidores_list = equipos_servidores_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('EquiposServidores', equipos_servidores_list)
    paginator = Paginator(equipos_servidores_list, 10)  # Muestra 10 equipos servidores por página

    page_number = request.GET.get('page')
    try:
        equipos_servidores = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        equipos_servidores = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        equipos_servidores = paginator.page(paginator.num_pages)

    if rol != 1:
        return render(request, 'equiposs/equipos_servidores_list.html', {
        'equipos_servidores': equipos_servidores,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Equipo de computo servidor',
        'clave': '1040',
        'nav':rol
        })
    return render(request, 'equiposs/equipos_servidores_list.html', {
        'equipos_servidores': equipos_servidores,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Equipo de computo servidor',
        'clave': '1040',
        'nav':rol
        })


@login_required
def equipo_servidor_detail(request, pk):
    equipo_servidor = EquiposServidores.objects.get(pk=pk)
    return render(request, 'equiposs/equipo_servidor_detail.html', {'equipo_servidor': equipo_servidor})

@login_required
def equipo_servidor_create(request):
    if request.method == 'POST':
        form = EquiposServidoresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_list')
    else:
        form = EquiposServidoresForms()
    return render(request, 'equiposs/equipo_servidor_form.html', {'form': form})

@login_required
def equipo_servidor_update(request, pk):
    equipo_servidor = EquiposServidores.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposServidoresForms(request.POST, instance=equipo_servidor)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_list')
    else:
        form = EquiposServidoresForms(instance=equipo_servidor)
    return render(request, 'equiposs/equipo_servidor_form.html', {'form': form})

@login_required
def equipo_servidor_delete(request, pk):
    equipo_servidor = EquiposServidores.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_servidor.delete()
        return redirect('equipos_servidores_list')
    return render(request, 'equiposs/equipo_servidor_confirm_delete.html', {'equipo_servidor': equipo_servidor})

########################
# End of CRUD Operations for EquiposServidores Model
########################

########################
# CRUD Operations for EquiposServidoresMarcas Model
########################

@login_required
def equipos_servidores_marcas_list(request):
    rol = usu(request)
    equipos_servidores_marcas_list = EquiposServidoresMarcas.objects.all()
    paginator = Paginator(equipos_servidores_marcas_list, 10)  # Muestra 10 marcas de servidores por página

    page_number = request.GET.get('page')
    try:
        equipos_servidores_marcas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        equipos_servidores_marcas = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        equipos_servidores_marcas = paginator.page(paginator.num_pages)

    return render(request, 'equiposs_marcas/equipos_servidores_marcas_list.html', {'equipos_servidores_marcas': equipos_servidores_marcas})


@login_required
def equipo_servidor_marca_detail(request, pk):
    equipo_servidor_marca = EquiposServidoresMarcas.objects.get(pk=pk)
    return render(request, 'equiposs_marcas/equipo_servidor_marca_detail.html', {'equipo_servidor_marca': equipo_servidor_marca})

@login_required
def equipo_servidor_marca_create(request):
    if request.method == 'POST':
        form = EquiposServidoresMarcasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_marcas_list')
    else:
        form = EquiposServidoresMarcasForms()
    return render(request, 'equiposs_marcas/equipo_servidor_marca_form.html', {'form': form})

@login_required
def equipo_servidor_marca_update(request, pk):
    equipo_servidor_marca = EquiposServidoresMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposServidoresMarcasForms(request.POST, instance=equipo_servidor_marca)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_marcas_list')
    else:
        form = EquiposServidoresMarcasForms(instance=equipo_servidor_marca)
    return render(request, 'equiposs_marcas/equipo_servidor_marca_form.html', {'form': form})

@login_required
def equipo_servidor_marca_delete(request, pk):
    equipo_servidor_marca = EquiposServidoresMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_servidor_marca.delete()
        return redirect('equipos_servidores_marcas_list')
    return render(request, 'equiposs_marcas/equipo_servidor_marca_confirm_delete.html', {'equipo_servidor_marca': equipo_servidor_marca})

########################
# End of CRUD Operations for EquiposServidoresMarcas Model
########################

########################
# CRUD Operations for EquiposServidoresProcesadores Model
########################

@login_required
def equipos_servidores_procesadores_list(request):
    rol = usu(request)
    equipos_servidores_procesadores_list = EquiposServidoresProcesadores.objects.all()
    paginator = Paginator(equipos_servidores_procesadores_list, 10)  # Muestra 10 procesadores de servidores por página

    page_number = request.GET.get('page')
    try:
        equipos_servidores_procesadores = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        equipos_servidores_procesadores = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        equipos_servidores_procesadores = paginator.page(paginator.num_pages)

    return render(request, 'equiposs_procesadores/equipos_servidores_procesadores_list.html', {'equipos_servidores_procesadores': equipos_servidores_procesadores})

@login_required
def equipo_servidor_procesador_detail(request, pk):
    equipo_servidor_procesador = EquiposServidoresProcesadores.objects.get(pk=pk)
    return render(request, 'equiposs_procesadores/equipo_servidor_procesador_detail.html', {'equipo_servidor_procesador': equipo_servidor_procesador})

@login_required
def equipo_servidor_procesador_create(request):
    if request.method == 'POST':
        form = EquiposServidoresProcesadoresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_procesadores_list')
    else:
        form = EquiposServidoresProcesadoresForms()
    return render(request, 'equiposs_procesadores/equipo_servidor_procesador_form.html', {'form': form})

@login_required
def equipo_servidor_procesador_update(request, pk):
    equipo_servidor_procesador = EquiposServidoresProcesadores.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposServidoresProcesadoresForms(request.POST, instance=equipo_servidor_procesador)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_procesadores_list')
    else:
        form = EquiposServidoresProcesadoresForms(instance=equipo_servidor_procesador)
    return render(request, 'equiposs_procesadores/equipo_servidor_procesador_form.html', {'form': form})

@login_required
def equipo_servidor_procesador_delete(request, pk):
    equipo_servidor_procesador = EquiposServidoresProcesadores.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_servidor_procesador.delete()
        return redirect('equipos_servidores_procesadores_list')
    return render(request, 'equiposs_procesadores/equipo_servidor_procesador_confirm_delete.html', {'equipo_servidor_procesador': equipo_servidor_procesador})

########################
# End of CRUD Operations for EquiposServidoresPuerto Model
########################

@login_required
def equipos_servidores_puertos_list(request):
    rol = usu(request)
    equipos_servidores_puertos_list = EquiposServidoresPuertos.objects.all()
    paginator = Paginator(equipos_servidores_puertos_list, 10)  # Muestra 10 procesadores de servidores por página

    page_number = request.GET.get('page')
    try:
        equipos_servidores_puertos = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        equipos_servidores_puertos = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        equipos_servidores_puertos = paginator.page(paginator.num_pages)

    return render(request, 'equiposs_puertos/equipos_servidores_puertos_list.html', {'equipos_servidores_puertos': equipos_servidores_puertos})

@login_required
def equipo_servidor_puerto_detail(request, pk):
    equipo_servidor_puerto = EquiposServidoresPuertos.objects.get(pk=pk)
    return render(request, 'equiposs_puertos/equipo_servidor_puerto_detail.html', {'equipo_servidor_puerto': equipo_servidor_puerto})

@login_required
def equipo_servidor_puerto_create(request):
    if request.method == 'POST':
        form = EquiposServidoresPuertosForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_puertos_list')
    else:
        form = EquiposServidoresPuertosForms()
    return render(request, 'equiposs_puertos/equipo_servidor_puerto_form.html', {'form': form})

@login_required
def equipo_servidor_puerto_update(request, pk):
    equipo_servidor_puerto = EquiposServidoresPuertos.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposServidoresPuertosForms(request.POST, instance=equipo_servidor_puerto)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_puertos_list')
    else:
        form = EquiposServidoresPuertosForms(instance=equipo_servidor_puerto)
    return render(request, 'equiposs_puertos/equipo_servidor_puerto_form.html', {'form': form})

@login_required
def equipo_servidor_puerto_delete(request, pk):
    equipo_servidor_puerto = EquiposServidoresPuertos.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_servidor_puerto.delete()
        return redirect('equipos_servidores_puertos_list')
    return render(request, 'equiposs_puerto/equipo_servidor_puerto_confirm_delete.html', {'equipo_servidor_puerto': equipo_servidor_puerto})

########################
# End of CRUD Operations for EquiposServidoresProcesadores Model
########################

########################
# CRUD Operations for EquiposServidoresTipos Model
########################

@login_required
def equipos_servidores_tipos_list(request):
    rol = usu(request)
    equipos_servidores_tipos_list = EquiposServidoresTipos.objects.all()
    paginator = Paginator(equipos_servidores_tipos_list, 10)  # Muestra 10 tipos de servidores por página

    page_number = request.GET.get('page')
    try:
        equipos_servidores_tipos = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        equipos_servidores_tipos = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        equipos_servidores_tipos = paginator.page(paginator.num_pages)

    return render(request, 'equiposs_tipos/equipos_servidores_tipos_list.html', {'equipos_servidores_tipos': equipos_servidores_tipos})


@login_required
def equipo_servidor_tipo_detail(request, pk):
    equipo_servidor_tipo = EquiposServidoresTipos.objects.get(pk=pk)
    return render(request, 'equiposs_tipos/equipo_servidor_tipo_detail.html', {'equipo_servidor_tipo': equipo_servidor_tipo})

@login_required
def equipo_servidor_tipo_create(request):
    if request.method == 'POST':
        form = EquiposServidoresTiposForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_tipos_list')
    else:
        form = EquiposServidoresTiposForms()
    return render(request, 'equiposs_tipos/equipo_servidor_tipo_form.html', {'form': form}) 

@login_required
def equipo_servidor_tipo_update(request, pk):
    equipo_servidor_tipo = EquiposServidoresTipos.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposServidoresTiposForms(request.POST, instance=equipo_servidor_tipo)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_tipos_list')
    else:
        form = EquiposServidoresTiposForms(instance=equipo_servidor_tipo)
    return render(request, 'equiposs_tipos/equipo_servidor_tipo_form.html', {'form': form})

@login_required
def equipo_servidor_tipo_delete(request, pk):
    equipo_servidor_tipo = EquiposServidoresTipos.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_servidor_tipo.delete()
        return redirect('equipos_servidores_tipos_list')
    return render(request, 'equiposs_tipos/equipo_servidor_tipo_confirm_delete.html', {'equipo_servidor_tipo': equipo_servidor_tipo})

########################
# End of CRUD Operations for EquiposServidoresTipos Model
########################

########################
# CRUD Operations for Firewalls Model
########################

@login_required
def firewalls_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    #firewalls_list = Firewalls.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            firewalls_list = Firewalls.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            firewalls_list = Firewalls.objects.filter(fecha__year=year)
    else:
        firewalls_list = Firewalls.objects.all()

    if secretaria:
        firewalls_list = firewalls_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        firewalls_list = firewalls_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('Firewalls', firewalls_list)
    paginator = Paginator(firewalls_list, 10)  # Muestra 10 firewalls por página

    page_number = request.GET.get('page')
    try:
        firewalls = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        firewalls = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        firewalls = paginator.page(paginator.num_pages)

    if rol != 1:
        return render(request, 'firewalls/firewalls_list.html', {
        'firewalls': firewalls,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Firewalls',
        'clave': '1090',
        'nav':rol
        })
    return render(request, 'firewalls/firewalls_list.html', {
        'firewalls': firewalls,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Firewalls',
        'clave': '1090',
        })

@login_required
def firewall_detail(request, pk):
    firewall = Firewalls.objects.get(pk=pk)
    return render(request, 'firewalls/firewall_detail.html', {'firewall': firewall})

@login_required
def firewall_create(request):
    if request.method == 'POST':
        form = FirewallsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('firewalls_list')
    else:
        form = FirewallsForms()
    return render(request, 'firewalls/firewall_form.html', {'form': form})

@login_required
def firewall_update(request, pk):
    firewall = Firewalls.objects.get(pk=pk)
    if request.method == 'POST':
        form = FirewallsForms(request.POST, instance=firewall)
        if form.is_valid():
            form.save()
            return redirect('firewalls_list')
    else:
        form = FirewallsForms(instance=firewall)
    return render(request, 'firewalls/firewall_form.html', {'form': form})

@login_required
def firewall_delete(request, pk):
    firewall = Firewalls.objects.get(pk=pk)
    if request.method == 'POST':
        firewall.delete()
        return redirect('firewalls_list')
    return render(request, 'firewalls/firewall_confirm_delete.html', {'firewall': firewall})

########################
# End of CRUD Operations for Firewalls Model
########################

########################
# CRUD Operations for FirewallsMarcas Model
########################

@login_required
def firewalls_marcas_list(request):
    rol = usu(request)
    firewalls_marcas_list = FirewallsMarcas.objects.all()
    paginator = Paginator(firewalls_marcas_list, 10)  # Muestra 10 marcas de firewalls por página

    page_number = request.GET.get('page')
    try:
        firewalls_marcas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        firewalls_marcas = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        firewalls_marcas = paginator.page(paginator.num_pages)

    return render(request, 'firewalls_marcas/firewalls_marcas_list.html', {'firewalls_marcas': firewalls_marcas})


@login_required
def firewall_marca_detail(request, pk):
    firewall_marca = FirewallsMarcas.objects.get(pk=pk)
    return render(request, 'firewalls_marcas/firewall_marca_detail.html', {'firewall_marca': firewall_marca})

@login_required
def firewall_marca_create(request):
    if request.method == 'POST':
        form = FirewallsMarcasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('firewalls_marcas_list')
    else:
        form = FirewallsMarcasForms()
    return render(request, 'firewalls_marcas/firewall_marca_form.html', {'form': form})

@login_required
def firewall_marca_update(request, pk):
    firewall_marca = FirewallsMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = FirewallsMarcasForms(request.POST, instance=firewall_marca)
        if form.is_valid():
            form.save()
            return redirect('firewalls_marcas_list')
    else:
        form = FirewallsMarcasForms(instance=firewall_marca)
    return render(request, 'firewalls_marcas/firewall_marca_form.html', {'form': form})

@login_required
def firewall_marca_delete(request, pk):
    firewall_marca = FirewallsMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        firewall_marca.delete()
        return redirect('firewalls_marcas_list')
    return render(request, 'firewalls_marcas/firewall_marca_confirm_delete.html', {'firewall_marca': firewall_marca})

########################
# End of CRUD Operations for FirewallsMarcas Model
########################

########################
# CRUD Operations for HerramientaDeDesarrollo Model
########################

@login_required
def herramientas_desarrollo_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    #herramientas_desarrollo_list = HerramientaDeDesarrollo.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            herramientas_desarrollo_list = HerramientaDeDesarrollo.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            herramientas_desarrollo_list = HerramientaDeDesarrollo.objects.filter(fecha__year=year)
    else:
        herramientas_desarrollo_list = HerramientaDeDesarrollo.objects.all()

    if secretaria:
        herramientas_desarrollo_list = herramientas_desarrollo_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        herramientas_desarrollo_list = herramientas_desarrollo_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('HerramientaDeDesarrollo', herramientas_desarrollo_list)
    paginator = Paginator(herramientas_desarrollo_list, 10)  # Muestra 10 herramientas de desarrollo por página

    page_number = request.GET.get('page')
    try:
        herramientas_desarrollo = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        herramientas_desarrollo = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        herramientas_desarrollo = paginator.page(paginator.num_pages)

    if rol != 1:
        return render(request, 'herramientas/herramientas_desarrollo_list.html', {
        'herramientas_desarrollo': herramientas_desarrollo,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Herramientas de desarrollo',
        'clave': '1110',
        'nav':rol
        })
    return render(request, 'herramientas/herramientas_desarrollo_list.html', {
        'herramientas_desarrollo': herramientas_desarrollo,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Herramientas de desarrollo',
        'clave': '1110',
        })


@login_required
def herramienta_desarrollo_detail(request, pk):
    herramienta_desarrollo = HerramientaDeDesarrollo.objects.get(pk=pk)
    return render(request, 'herramientas/herramienta_desarrollo_detail.html', {'herramienta_desarrollo': herramienta_desarrollo})

@login_required
def herramienta_desarrollo_create(request):
    if request.method == 'POST':
        form = HerramientaDeDesarrolloForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('herramientas_desarrollo_list')
    else:
        form = HerramientaDeDesarrolloForms()
    return render(request, 'herramientas/herramienta_desarrollo_form.html', {'form': form})

@login_required
def herramienta_desarrollo_update(request, pk):
    herramienta_desarrollo = HerramientaDeDesarrollo.objects.get(pk=pk)
    if request.method == 'POST':
        form = HerramientaDeDesarrolloForms(request.POST, instance=herramienta_desarrollo)
        if form.is_valid():
            form.save()
            return redirect('herramientas_desarrollo_list')
    else:
        form = HerramientaDeDesarrolloForms(instance=herramienta_desarrollo)
    return render(request, 'herramientas/herramienta_desarrollo_form.html', {'form': form})

@login_required
def herramienta_desarrollo_delete(request, pk):
    herramienta_desarrollo = HerramientaDeDesarrollo.objects.get(pk=pk)
    if request.method == 'POST':
        herramienta_desarrollo.delete()
        return redirect('herramientas_desarrollo_list')
    return render(request, 'herramientas/herramienta_desarrollo_confirm_delete.html', {'herramienta_desarrollo': herramienta_desarrollo})

########################
# End of CRUD Operations for HerramientaDeDesarrollo Model
########################

########################
# CRUD Operations for Impresoras Model
########################

@login_required
def impresoras_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    #impresoras_list = Impresoras.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            impresoras_list = Impresoras.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            impresoras_list = Impresoras.objects.filter(fecha__year=year)
    else:
        impresoras_list = Impresoras.objects.all()

    if secretaria:
        impresoras_list = impresoras_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        impresoras_list = impresoras_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('Impresoras', impresoras_list)
    paginator = Paginator(impresoras_list, 10)  # Muestra 10 impresoras por página

    page_number = request.GET.get('page')
    try:
        impresoras = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        impresoras = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        impresoras = paginator.page(paginator.num_pages)
    if rol != 1:
        return render(request, 'impresoras/impresoras_list.html', {
        'impresoras': impresoras,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Impresoras',
        'clave': '1050',
        'nav':rol
        })
    return render(request, 'impresoras/impresoras_list.html', {
        'impresoras': impresoras,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Impresoras',
        'clave': '1050',
        })

@login_required
def impresora_detail(request, pk):
    impresora = Impresoras.objects.get(pk=pk)
    return render(request, 'impresoras/impresora_detail.html', {'impresora': impresora})

@login_required
def impresora_create(request):
    if request.method == 'POST':
        form = ImpresorasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('impresoras_list')
    else:
        form = ImpresorasForms()
    return render(request, 'impresoras/impresora_form.html', {'form': form})

@login_required
def impresora_update(request, pk):
    impresora = Impresoras.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImpresorasForms(request.POST, instance=impresora)
        if form.is_valid():
            form.save()
            return redirect('impresoras_list')
    else:
        form = ImpresorasForms(instance=impresora)
    return render(request, 'impresoras/impresora_form.html', {'form': form})

@login_required
def impresora_delete(request, pk):
    impresora = Impresoras.objects.get(pk=pk)
    if request.method == 'POST':
        impresora.delete()
        return redirect('impresoras_list')
    return render(request, 'impresoras/impresora_confirm_delete.html', {'impresora': impresora})

########################
# End of CRUD Operations for Impresoras Model
########################

########################
# CRUD Operations for ImpresorasMarcas Model
########################

@login_required
def impresoras_marcas_list(request):
    rol = usu(request)
    impresoras_marcas_list = ImpresorasMarcas.objects.all()
    paginator = Paginator(impresoras_marcas_list, 10)  # Muestra 10 marcas de impresoras por página

    page_number = request.GET.get('page')
    try:
        impresoras_marcas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        impresoras_marcas = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        impresoras_marcas = paginator.page(paginator.num_pages)

    return render(request, 'impresoras_marcas/impresoras_marcas_list.html', {'impresoras_marcas': impresoras_marcas})

@login_required
def impresora_marca_detail(request, pk):
    impresora_marca = ImpresorasMarcas.objects.get(pk=pk)
    return render(request, 'impresoras_marcas/impresora_marca_detail.html', {'impresora_marca': impresora_marca})

@login_required
def impresora_marca_create(request):
    if request.method == 'POST':
        form = ImpresorasMarcasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('impresoras_marcas_list')
    else:
        form = ImpresorasMarcasForms()
    return render(request, 'impresoras_marcas/impresora_marca_form.html', {'form': form})

@login_required
def impresora_marca_update(request, pk):
    impresora_marca = ImpresorasMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImpresorasMarcasForms(request.POST, instance=impresora_marca)
        if form.is_valid():
            form.save()
            return redirect('impresoras_marcas_list')
    else:
        form = ImpresorasMarcasForms(instance=impresora_marca)
    return render(request, 'impresoras_marcas/impresora_marca_form.html', {'form': form})

@login_required
def impresora_marca_delete(request, pk):
    impresora_marca = ImpresorasMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        impresora_marca.delete()
        return redirect('impresoras_marcas_list')
    return render(request, 'impresoras_marcas/impresora_marca_confirm_delete.html', {'impresora_marca': impresora_marca})

########################
# End of CRUD Operations for ImpresorasMarcas Model
########################

########################
# CRUD Operations for Municipios
########################

@login_required
def municipios_list(request):
    rol = usu(request)
    municipios_list = Municipios.objects.all()
    paginator = Paginator(municipios_list, 10)  # Muestra 10 tipos de enlaces por página

    page_number = request.GET.get('page')
    try:
        municipios = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        municipios = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        municipios = paginator.page(paginator.num_pages)

    return render(request, 'municipios/municipios_list.html', {'municipios': municipios})

@login_required
def municipio_detail(request, pk):
    municipio = Municipios.objects.get(pk=pk)
    return render(request, 'municipios/municipio_detail.html', {'municipio': municipio})

@login_required
def municipio__create(request):
    if request.method == 'POST':
        form = MunicipiosForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('municipios_list')
    else:
        form = MunicipiosForms()
    return render(request, 'municipios/municipio_form.html', {'form': form})

@login_required
def municipio_update(request, pk):
    municipio = Municipios.objects.get(pk=pk)
    if request.method == 'POST':
        form = MunicipiosForms(request.POST, instance=municipio)
        if form.is_valid():
            form.save()
            return redirect('municipios_list')
    else:
        form = MunicipiosForms(instance=municipio)
    return render(request, 'municipios/municipio_form.html', {'form': form})

@login_required
def municipio_delete(request, pk):
    municipio = Municipios.objects.get(pk=pk)
    if request.method == 'POST':
        municipio.delete()
        return redirect('municipios_list')
    return render(request, 'municipios/municipio_confirm_delete.html', {'municipio': municipio})

########################
# End of CRUD Operations for Municipios
########################

########################
# CRUD Operations for Proyectores Model
########################

@login_required
def proyectores_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    proyectores_list = Proyectores.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            proyectores_list = Proyectores.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            proyectores_list = Proyectores.objects.filter(fecha__year=year)
    else:
        proyectores_list = Proyectores.objects.all()

    if secretaria:
        proyectores_list = proyectores_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        proyectores_list = proyectores_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('Proyectores', proyectores_list)
    paginator = Paginator(proyectores_list, 10)  # Muestra 10 proyectores por página

    page_number = request.GET.get('page')
    try:
        proyectores = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        proyectores = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        proyectores = paginator.page(paginator.num_pages)

    if rol != 1:
        return render(request, 'proyectores/proyectores_list.html', {
        'proyectores': proyectores,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Proyectores',
        'clave': '1060',
        'nav':rol
        })
    return render(request, 'proyectores/proyectores_list.html', {
        'proyectores': proyectores,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Proyectores',
        'clave': '1060',
        })


@login_required
def proyector_detail(request, pk):
    proyector = Proyectores.objects.get(pk=pk)
    return render(request, 'proyectores/proyector_detail.html', {'proyector': proyector})

@login_required
def proyector_create(request):
    if request.method == 'POST':
        form = ProyectoresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyectores_list')
    else:
        form = ProyectoresForms()
    return render(request, 'proyectores/proyector_form.html', {'form': form})

@login_required
def proyector_update(request, pk):
    proyector = Proyectores.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProyectoresForms(request.POST, instance=proyector)
        if form.is_valid():
            form.save()
            return redirect('proyectores_list')
    else:
        form = ProyectoresForms(instance=proyector)
    return render(request, 'proyectores/proyector_form.html', {'form': form})

@login_required
def proyector_delete(request, pk):
    proyector = Proyectores.objects.get(pk=pk)
    if request.method == 'POST':
        proyector.delete()
        return redirect('proyectores_list')
    return render(request, 'proyectores/proyector_confirm_delete.html', {'proyector': proyector})

########################
# End of CRUD Operations for Proyectores Model
########################


########################
# CRUD Operations for Proyectores  Marcas Model
########################

@login_required
def proyectores_marcas_list(request):
    rol = usu(request)
    proyectores_marcas_list = ProyectoresMarcas.objects.all()
    paginator = Paginator(proyectores_marcas_list, 10)  # Muestra 10 proyectores por página

    page_number = request.GET.get('page')
    try:
        proyectores_marcas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        proyectores_marcas = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        proyectores_marcas = paginator.page(paginator.num_pages)

    return render(request, 'proyectores_marcas/proyectores_marcas_list.html', {'proyectores_marcas': proyectores_marcas})


@login_required
def proyector_marca_detail(request, pk):
    proyector_marca = ProyectoresMarcas.objects.get(pk=pk)
    return render(request, 'proyectores_marcas/proyector_detail.html', {'proyector_marca': proyector_marca})

@login_required
def proyector_marca_create(request):
    if request.method == 'POST':
        form = ProyectoresMarcasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyectores_marcas_list')
    else:
        form = ProyectoresMarcasForms()
    return render(request, 'proyectores_marcas/proyector_marca_form.html', {'form': form})

@login_required
def proyector_marca_update(request, pk):
    proyector_marca = ProyectoresMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProyectoresMarcasForms(request.POST, instance=proyector_marca)
        if form.is_valid():
            form.save()
            return redirect('proyectores_marcas_list')
    else:
        form = ProyectoresMarcasForms(instance=proyector_marca)
    return render(request, 'proyectores_marcas/proyector_marca_form.html', {'form': form})

@login_required
def proyector_marca_delete(request, pk):
    proyector_marca = ProyectoresMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        proyector_marca.delete()
        return redirect('proyectores_marcas_list')
    return render(request, 'proyectores_marcas/proyector_marca_confirm_delete.html', {'proyector_marca': proyector_marca})

########################
# End of CRUD Operations for Proyectores  Marca Model
########################


########################
# CRUD Operations for Routers Model
########################

@login_required
def routers_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    routers_list = Routers.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            routers_list = Routers.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            routers_list = Routers.objects.filter(fecha__year=year)
    else:
        routers_list = Routers.objects.all()

    if secretaria:
        routers_list = routers_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        routers_list = routers_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('Routers', routers_list)
    paginator = Paginator(routers_list, 10)  # Muestra 10 routers por página

    page_number = request.GET.get('page')
    try:
        routers = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        routers = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        routers = paginator.page(paginator.num_pages)
    if rol != 1:
        return render(request, 'routers/routers_list.html', {
        'routers': routers,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Routers',
        'clave': '1091',
        'nav':rol
        })
    return render(request, 'routers/routers_list.html', {
        'routers': routers,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Routers',
        'clave': '1091',
        })

@login_required
def router_detail(request, pk):
    router = Routers.objects.get(pk=pk)
    return render(request, 'routers/routers_detail.html', {'router': router})

@login_required
def router_create(request):
    if request.method == 'POST':
        form = RoutersForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('routers_list')
    else:
        form = RoutersForms()
    return render(request, 'routers/routers_form.html', {'form': form})

@login_required
def router_update(request, pk):
    router = Routers.objects.get(pk=pk)
    if request.method == 'POST':
        form = RoutersForms(request.POST, instance=router)
        if form.is_valid():
            form.save()
            return redirect('routers_list')
    else:
        form = RoutersForms(instance=router)
    return render(request, 'routers/routers_form.html', {'form': form})

@login_required
def router_delete(request, pk):
    router = Routers.objects.get(pk=pk)
    if request.method == 'POST':
        router.delete()
        return redirect('routers_list')
    return render(request, 'routers/routers_confirm_delete.html', {'router': router})

########################
# End of CRUD Operations for Routers Model
########################


########################
# CRUD Operations for Roles Model
########################

@login_required
def roles_list(request):
    rol = usu(request)
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    roles_list = Roles.objects.all()

    if search:
        roles_list = roles_list.filter(no_inventario__icontains=search)
    

    paginator = Paginator(roles_list, 10)  # Muestra 10 routers por página

    page_number = request.GET.get('page')
    try:
        roles = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        roles = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        roles = paginator.page(paginator.num_pages)

    return render(request, 'roles/roles_list.html', {'roles': roles})

@login_required
def rol_detail(request, pk):
    rol = Roles.objects.get(pk=pk)
    return render(request, 'roles/rol_detail.html', {'rol': rol})

@login_required
def rol_create(request):
    if request.method == 'POST':
        form = RolesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roles_list')
    else:
        form = RolesForms()
    return render(request, 'roles/rol_form.html', {'form': form})

@login_required
def rol_update(request, pk):
    rol = Roles.objects.get(pk=pk)
    if request.method == 'POST':
        form = RolesForms(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('roles_list')
    else:
        form = RolesForms(instance=rol)
    return render(request, 'roles/rol_form.html', {'form': form})

@login_required
def rol_delete(request, pk):
    rol = Roles.objects.get(pk=pk)
    if request.method == 'POST':
        rol.delete()
        return redirect('roles_list')
    return render(request, 'roles/rol_confirm_delete.html', {'rol': rol})

########################
# End of CRUD Operations for Routers Model
########################

########################
# CRUD Operations for Secretarias Model
########################

@login_required
def secretarias_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    return render(request, 'secretarias/secretarias_list.html', {'secretarias': secretarias})

@login_required
def secretaria_detail(request, pk):
    secretaria = Secretarias.objects.get(pk=pk)
    return render(request, 'secretarias/secretaria_detail.html', {'secretaria': secretaria})

@login_required
def secretaria_create(request):
    if request.method == 'POST':
        form = SecretariasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secretarias_list')
    else:
        form = SecretariasForms()
    return render(request, 'secretarias/secretaria_form.html', {'form': form})

@login_required
def secretaria_update(request, pk):
    secretaria = Secretarias.objects.get(pk=pk)
    if request.method == 'POST':
        form = SecretariasForms(request.POST, instance=secretaria)
        if form.is_valid():
            form.save()
            return redirect('secretarias_list')
    else:
        form = SecretariasForms(instance=secretaria)
    return render(request, 'secretarias/secretaria_form.html', {'form': form})

@login_required
def secretaria_delete(request, pk):
    secretaria = Secretarias.objects.get(pk=pk)
    if request.method == 'POST':
        secretaria.delete()
        return redirect('secretarias_list')
    return render(request, 'secretarias/secretaria_confirm_delete.html', {'secretaria': secretaria})

########################
# End of CRUD Operations for Secretarias Model
########################

########################
# CRUD Operations for Dependencias Model
########################

@login_required
def dependencias_list(request):
    rol = usu(request)
    secretarias = Dependencias.objects.all()
    paginator = Paginator(secretarias, 10)  # Muestra 10 routers por página

    page_number = request.GET.get('page')
    try:
        secretarias = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        secretarias = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        secretarias = paginator.page(paginator.num_pages)
    return render(request, 'dependencias/dependencias_list.html', {'secretarias': secretarias})

@login_required
def dependencia_detail(request, pk):
    secretaria = Dependencias.objects.get(pk=pk)
    return render(request, 'dependencias/dependencias_detail.html', {'secretaria': secretaria})

@login_required
def dependencia_create(request):
    if request.method == 'POST':
        form = DependenciasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dependencias_list')
    else:
        form = DependenciasForms()
    return render(request, 'dependencias/dependencias_form.html', {'form': form})

@login_required
def dependencia_update(request, pk):
    secretaria = Dependencias.objects.get(pk=pk)
    if request.method == 'POST':
        form = DependenciasForms(request.POST, instance=secretaria)
        if form.is_valid():
            form.save()
            return redirect('dependencias_list')
    else:
        form = DependenciasForms(instance=secretaria)
    return render(request, 'dependencias/dependencias_form.html', {'form': form})

@login_required
def dependencia_delete(request, pk):
    secretaria = Dependencias.objects.get(pk=pk)
    if request.method == 'POST':
        secretaria.delete()
        return redirect('dependencias_list')
    return render(request, 'dependencias/secretaria_confirm_delete.html', {'secretaria': secretaria})

########################
# End of CRUD Operations for Dependencias Model
########################

########################
# CRUD Operations for SistemaDeInformacionMovil Model
########################

@login_required
def sistemas_informacion_movil_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            sistemas_informacion_movil_list = SistemaDeInformacionMovil.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            sistemas_informacion_movil_list = SistemaDeInformacionMovil.objects.filter(fecha__year=year)
    else:
        sistemas_informacion_movil_list = SistemaDeInformacionMovil.objects.all()
    
    if secretaria:
        sistemas_informacion_movil_list = sistemas_informacion_movil_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        sistemas_informacion_movil_list = sistemas_informacion_movil_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('SistemaDeInformacionMovil', sistemas_informacion_movil_list)
    paginator = Paginator(sistemas_informacion_movil_list, 10)  # Muestra 10 sistemas de información móvil por página

    page_number = request.GET.get('page')
    try:
        sistemas_informacion_movil = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        sistemas_informacion_movil = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        sistemas_informacion_movil = paginator.page(paginator.num_pages)
    if rol != 1:
        return render(request, 'sistemas_informacion_movil/sistemas_informacion_movil_list.html', {
        'sistemas_informacion_movil': sistemas_informacion_movil,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Sistema De Informacion Movil',
        'clave': '1130',
        'nav':rol,
        })
    return render(request, 'sistemas_informacion_movil/sistemas_informacion_movil_list.html', {
        'sistemas_informacion_movil': sistemas_informacion_movil,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Sistema De Informacion Movil',
        'clave': '1130',
        })

@login_required
def sistema_informacion_movil_detail(request, pk):
    sistema_informacion_movil = SistemaDeInformacionMovil.objects.get(pk=pk)
    return render(request, 'sistemas_informacion_movil/sistema_informacion_movil_detail.html', {'sistema_informacion_movil': sistema_informacion_movil})

@login_required
def sistema_informacion_movil_create(request):
    if request.method == 'POST':
        form = SistemaDeInformacionMovilForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistemas_informacion_movil_list')
    else:
        form = SistemaDeInformacionMovilForms()
    return render(request, 'sistemas_informacion_movil/sistema_informacion_movil_form.html', {'form': form})

@login_required
def sistema_informacion_movil_update(request, pk):
    sistema_informacion_movil = SistemaDeInformacionMovil.objects.get(pk=pk)
    if request.method == 'POST':
        form = SistemaDeInformacionMovilForms(request.POST, instance=sistema_informacion_movil)
        if form.is_valid():
            form.save()
            return redirect('sistemas_informacion_movil_list')
    else:
        form = SistemaDeInformacionMovilForms(instance=sistema_informacion_movil)
    return render(request, 'sistemas_informacion_movil/sistema_informacion_movil_form.html', {'form': form})

@login_required
def sistema_informacion_movil_delete(request, pk):
    sistema_informacion_movil = SistemaDeInformacionMovil.objects.get(pk=pk)
    if request.method == 'POST':
        sistema_informacion_movil.delete()
        return redirect('sistemas_informacion_movil_list')
    return render(request, 'sistemas_informacion_movil/sistema_informacion_movil_confirm_delete.html', {'sistema_informacion_movil': sistema_informacion_movil})

########################
# End of CRUD Operations for SistemaDeInformacionMovil Model
########################

########################
# CRUD Operations for SistemaInformacionMovilNombres Model
########################

@login_required
def sistemas_informacion_movil_nombres_list(request):
    rol = usu(request)
    sistemas_informacion_movil_nombres_list = SistemaInformacionMovilNombres.objects.all()
    paginator = Paginator(sistemas_informacion_movil_nombres_list, 10)  # Muestra 10 nombres de sistemas de información móvil por página

    page_number = request.GET.get('page')
    try:
        sistemas_informacion_movil_nombres = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        sistemas_informacion_movil_nombres = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        sistemas_informacion_movil_nombres = paginator.page(paginator.num_pages)

    return render(request, 'sistema_informacion_movil_nombres/sistemas_informacion_movil_nombres_list.html', {'sistemas_informacion_movil_nombres': sistemas_informacion_movil_nombres})


@login_required
def sistema_informacion_movil_nombre_detail(request, pk):
    sistema_informacion_movil_nombre = SistemaInformacionMovilNombres.objects.get(pk=pk)
    return render(request, 'sistema_informacion_movil_nombres/sistema_informacion_movil_nombre_detail.html', {'sistema_informacion_movil_nombre': sistema_informacion_movil_nombre})

@login_required
def sistema_informacion_movil_nombre_create(request):
    if request.method == 'POST':
        form = SistemaInformacionMovilNombresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistemas_informacion_movil_nombres_list')
    else:
        form = SistemaInformacionMovilNombresForms()
    return render(request, 'sistema_informacion_movil_nombres/sistema_informacion_movil_nombre_form.html', {'form': form})

@login_required
def sistema_informacion_movil_nombre_update(request, pk):
    sistema_informacion_movil_nombre = SistemaInformacionMovilNombres.objects.get(pk=pk)
    if request.method == 'POST':
        form = SistemaInformacionMovilNombresForms(request.POST, instance=sistema_informacion_movil_nombre)
        if form.is_valid():
            form.save()
            return redirect('sistemas_informacion_movil_nombres_list')
    else:
        form = SistemaInformacionMovilNombresForms(instance=sistema_informacion_movil_nombre)
    return render(request, 'sistema_informacion_movil_nombres/sistema_informacion_movil_nombre_form.html', {'form': form})

@login_required
def sistema_informacion_movil_nombre_delete(request, pk):
    sistema_informacion_movil_nombre = SistemaInformacionMovilNombres.objects.get(pk=pk)
    if request.method == 'POST':
        sistema_informacion_movil_nombre.delete()
        return redirect('sistemas_informacion_movil_nombres_list')
    return render(request, 'sistema_informacion_movil_nombres/sistema_informacion_movil_nombre_confirm_delete.html', {'sistema_informacion_movil_nombre': sistema_informacion_movil_nombre})

########################
# End of CRUD Operations for SistemaInformacionMovilNombres Model
########################

########################
# CRUD Operations for SistemasInformacion Model
########################

@login_required
def sistemas_informacion_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        
        
        if dependencia:
            sistemas_informacion_list = SistemasInformacion.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            sistemas_informacion_list = SistemasInformacion.objects.filter(fecha__year=year)
    else:
        sistemas_informacion_list = SistemasInformacion.objects.all()

    if secretaria:
        sistemas_informacion_list = sistemas_informacion_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        sistemas_informacion_list = sistemas_informacion_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('SistemasInformacion', sistemas_informacion_list)
    paginator = Paginator(sistemas_informacion_list, 10)  # Muestra 10 sistemas de información por página

    page_number = request.GET.get('page')
    try:
        sistemas_informacion = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        sistemas_informacion = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        sistemas_informacion = paginator.page(paginator.num_pages)

    if rol != 1:
        return render(request, 'sistemas_informacion/sistemas_informacion_list.html', {
        'sistemas_informacion': sistemas_informacion,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Sistemas de Informacion',
        'clave': '1120',
        'nav':rol,
        })
    return render(request, 'sistemas_informacion/sistemas_informacion_list.html', {
        'sistemas_informacion': sistemas_informacion,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Sistemas de Informacion',
        'clave': '1120',
        })

@login_required
def sistema_informacion_detail(request, pk):
    sistema_informacion = SistemasInformacion.objects.get(pk=pk)
    return render(request, 'sistemas_informacion/sistema_informacion_detail.html', {'sistema_informacion': sistema_informacion})

@login_required
def sistema_informacion_create(request):
    if request.method == 'POST':
        form = SistemasInformacionForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistemas_informacion_list')
    else:
        form = SistemasInformacionForms()
    return render(request, 'sistemas_informacion/sistema_informacion_form.html', {'form': form})

@login_required
def sistema_informacion_update(request, pk):
    sistema_informacion = SistemasInformacion.objects.get(pk=pk)
    if request.method == 'POST':
        form = SistemasInformacionForms(request.POST, instance=sistema_informacion)
        if form.is_valid():
            form.save()
            return redirect('sistemas_informacion_list')
    else:
        form = SistemasInformacionForms(instance=sistema_informacion)
    return render(request, 'sistemas_informacion/sistema_informacion_form.html', {'form': form})

@login_required
def sistema_informacion_delete(request, pk):
    sistema_informacion = SistemasInformacion.objects.get(pk=pk)
    if request.method == 'POST':
        sistema_informacion.delete()
        return redirect('sistemas_informacion_list')
    return render(request, 'sistemas_informacion/sistema_informacion_confirm_delete.html', {'sistema_informacion': sistema_informacion})

########################
# End of CRUD Operations for SistemasInformacion Model
########################

########################
# CRUD Operations for SistemasInformacionNombres Model
########################

@login_required
def sistemas_informacion_nombres_list(request):
    rol = usu(request)
    sistemas_informacion_nombres_list = SistemasInformacionNombres.objects.all()
    paginator = Paginator(sistemas_informacion_nombres_list, 10)  # Muestra 10 nombres de sistemas de información por página

    page_number = request.GET.get('page')
    try:
        sistemas_informacion_nombres = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        sistemas_informacion_nombres = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        sistemas_informacion_nombres = paginator.page(paginator.num_pages)

    return render(request, 'sistemas_informacion_nombres/sistemas_informacion_nombres_list.html', {'sistemas_informacion_nombres': sistemas_informacion_nombres})


@login_required
def sistema_informacion_nombre_detail(request, pk):
    sistema_informacion_nombre = SistemasInformacionNombres.objects.get(pk=pk)
    return render(request, 'sistemas_informacion_nombres/sistema_informacion_nombre_detail.html', {'sistema_informacion_nombre': sistema_informacion_nombre})

@login_required
def sistema_informacion_nombre_create(request):
    if request.method == 'POST':
        form = SistemasInformacionNombresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistemas_informacion_nombres_list')
    else:
        form = SistemasInformacionNombresForms()
    return render(request, 'sistemas_informacion_nombres/sistema_informacion_nombre_form.html', {'form': form})

@login_required
def sistema_informacion_nombre_update(request, pk):
    sistema_informacion_nombre = SistemasInformacionNombres.objects.get(pk=pk)
    if request.method == 'POST':
        form = SistemasInformacionNombresForms(request.POST, instance=sistema_informacion_nombre)
        if form.is_valid():
            form.save()
            return redirect('sistemas_informacion_nombres_list')
    else:
        form = SistemasInformacionNombresForms(instance=sistema_informacion_nombre)
    return render(request, 'sistemas_informacion_nombres/sistema_informacion_nombre_form.html', {'form': form})

@login_required
def sistema_informacion_nombre_delete(request, pk):
    sistema_informacion_nombre = SistemasInformacionNombres.objects.get(pk=pk)
    if request.method == 'POST':
        sistema_informacion_nombre.delete()
        return redirect('sistemas_informacion_nombres_list')
    return render(request, 'sistemas_informacion_nombres/sistema_informacion_nombre_confirm_delete.html', {'sistema_informacion_nombre': sistema_informacion_nombre})

########################
# End of CRUD Operations for SistemasInformacionNombres Model
########################

########################
# CRUD Operations for Sites Model
########################

@login_required
def sites_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    sites_list = Sites.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:       
        
        if dependencia:
            sites_list = Sites.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            sites_list = Sites.objects.filter(fecha__year=year)
    else:
        sites_list = Sites.objects.all()

    if secretaria:
        sites_list = sites_list.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        sites_list = sites_list.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('Sites', sites_list)
    paginator = Paginator(sites_list, 10)  # Muestra 10 sitios por página

    page_number = request.GET.get('page')
    try:
        sites = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        sites = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        sites = paginator.page(paginator.num_pages)

    if rol != 1:
        return render(request, 'sites/sites_list.html', {
        'sites': sites,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Sites',
        'clave': '1230',
        'nav':rol
        })
    return render(request, 'sites/sites_list.html', {
        'sites': sites,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Sites',
        'clave': '1230',
        })

@login_required
def site_detail(request, pk):
    site = Sites.objects.get(pk=pk)
    return render(request, 'sites/site_detail.html', {'site': site})

@login_required
def site_create(request):
    if request.method == 'POST':
        form = SitesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sites_list')
    else:
        form = SitesForms()
    return render(request, 'sites/site_form.html', {'form': form})

@login_required
def site_update(request, pk):
    site = Sites.objects.get(pk=pk)
    if request.method == 'POST':
        form = SitesForms(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('sites_list')
    else:
        form = SitesForms(instance=site)
    return render(request, 'sites/site_form.html', {'form': form})

@login_required
def site_delete(request, pk):
    site = Sites.objects.get(pk=pk)
    if request.method == 'POST':
        site.delete()
        return redirect('sites_list')
    return render(request, 'sites/site_confirm_delete.html', {'site': site})

########################
# End of CRUD Operations for Sites Model
########################

########################
# CRUD Operations for Usuarios Model
########################

@login_required
def usuarios_list(request):
    rol = usu(request)
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    dependencia = request.GET.get('dependencia')
    secretaria = request.GET.get('secretariaSelec')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    usuarios = Usuarios.objects.all()

    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)

    if dependencia:
        usuarios = Usuarios.objects.filter(id_dependencia=dependencia)

    else:
        usuarios = Usuarios.objects.all()

    if secretaria:
        usuarios = usuarios.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        usuarios = usuarios.filter(email__icontains=search)
    if request.GET.get('descarga') == '1':
        return generate_excel('Usuarios', usuarios)
    paginator = Paginator(usuarios, 10)  # Muestra 10 sitios por página

    page_number = request.GET.get('page')
    try:
        usuarios = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        usuarios = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        usuarios = paginator.page(paginator.num_pages)

    if rol != 1:
        return render(request, 'usuarios/usuarios_list.html', {
        'usuarios': usuarios,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Usuarios',
        'clave': '1310',
        'nav':rol
        })
    return render(request, 'usuarios/usuarios_list.html', {
        'usuarios': usuarios,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'selected_secretaria': request.GET.get('secretaria'),
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'categoria_seleccionada':categoria if categoria else '',
        'inventario': 'Usuarios',
        })


@login_required
def usuario_detail(request, pk):
    usuario = Usuarios.objects.get(pk=pk)
    return render(request, 'usuarios/usuario_detail.html', {'usuario': usuario})

@login_required
def usuario_create(request):
    if request.method == 'POST':
        form = UsuariosForms(request.POST)
        if form.is_valid():
            # Guardar el formulario de Usuarios para obtener el objeto de usuario creado
            usuario = form.save()
            # Crear un usuario en el modelo User y guardar su id en el campo 'usuario' de Usuarios
            nuevo_user = User.objects.create_user(username=usuario.email, password=usuario.contrasenia)
            # Actualizar el campo 'usuario' con el nombre de usuario del nuevo usuario
            usuario.usuario = nuevo_user.id
            # Obtener la contraseña cifrada del nuevo usuario
            contrasenia_cifrada = nuevo_user.password
            # Asignar la contraseña cifrada al campo 'contrasenia' del objeto 'usuario'
            usuario.contrasenia = make_password(contrasenia_cifrada)
            # Guardar los cambios en el objeto 'usuario'
            usuario.save()
            return redirect('usuarios_list')
    else:
        form = UsuariosForms()
    return render(request, 'usuarios/usuario_form.html', {'form': form})


@login_required
def usuario_update(request, pk):
    usuario = Usuarios.objects.get(pk=pk)
    if request.method == 'POST':
        form = UsuariosForms(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            # Actualizar el usuario correspondiente en el modelo User
            user = User.objects.get(id=usuario.usuario)
            user.set_password(usuario.contrasenia)
            user.save()
            return redirect('usuarios_list')
    else:
        form = UsuariosForms(instance=usuario)
    return render(request, 'usuarios/usuario_form.html', {'form': form})

@login_required
def usuario_delete(request, pk):
    usuario = Usuarios.objects.get(pk=pk)
    if request.method == 'POST':
        # Eliminar el usuario correspondiente en el modelo User
        user = User.objects.get(id=usuario.usuario)
        user.delete()
        usuario.delete()
        return redirect('usuarios_list')
    return render(request, 'usuarios/usuario_confirm_delete.html', {'usuario': usuario})

########################
# End of CRUD Operations for Usuarios Model
########################
