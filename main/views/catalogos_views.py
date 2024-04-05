from django.shortcuts import render, redirect
from ..models import *
from ..forms import *

########################
# CRUD Operations for ConmutadoresMarcas Model
########################

from django.shortcuts import render, redirect
from ..models import ConmutadoresMarcas
from ..forms import *

def conmutadores_marcas_list(request):
    conmutadores_marcas = ConmutadoresMarcas.objects.all()
    return render(request, 'conmutadores/conmutadores_marcas_list.html', {'conmutadores_marcas': conmutadores_marcas})

def conmutadores_marca_detail(request, pk):
    conmutador_marca = ConmutadoresMarcas.objects.get(pk=pk)
    return render(request, 'conmutadores/conmutadores_marca_detail.html', {'conmutador_marca': conmutador_marca})

def conmutadores_marca_create(request):
    if request.method == 'POST':
        form = ConmutadorMarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conmutadores_marcas_list')
    else:
        form = ConmutadorMarcaForm()
    return render(request, 'conmutadores/conmutadores_marca_form.html', {'form': form})

def conmutadores_marca_update(request, pk):
    conmutador_marca = ConmutadoresMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = ConmutadorMarcaForm(request.POST, instance=conmutador_marca)
        if form.is_valid():
            form.save()
            return redirect('conmutadores_marcas_list')
    else:
        form = ConmutadorMarcaForm(instance=conmutador_marca)
    return render(request, 'conmutadores/conmutadores_marca_form.html', {'form': form})

def conmutadores_marca_delete(request, pk):
    conmutador_marca = ConmutadoresMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        conmutador_marca.delete()
        return redirect('conmutadores_marcas_list')
    return render(request, 'conmutadores/conmutadores_marca_confirm_delete.html', {'conmutador_marca': conmutador_marca})

########################
# End of CRUD Operations for ConmutadoresMarcas Model
########################

########################
# CRUD Operations for Dependencias Model
########################
def dependencias_list(request):
    dependencias = Dependencias.objects.all()
    return render(request, 'dependencias/dependencias_list.html', {'dependencias': dependencias})

def dependencia_detail(request, pk):
    dependencia = Dependencias.objects.get(pk=pk)
    return render(request, 'dependencias/dependencia_detail.html', {'dependencia': dependencia})

def dependencia_create(request):
    if request.method == 'POST':
        form = DependenciasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dependencias_list')
    else:
        form = DependenciasForms()
    return render(request, 'dependencias/dependencia_form.html', {'form': form})

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

def drones_list(request):
    drones = Drones.objects.all()
    return render(request, 'drones/drones_list.html', {'drones': drones})

def drone_detail(request, pk):
    drone = Drones.objects.get(pk=pk)
    return render(request, 'drones/drone_detail.html', {'drone': drone})

def drone_create(request):
    if request.method == 'POST':
        form = DronesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drones_list')
    else:
        form = DronesForms()
    return render(request, 'drones/drone_form.html', {'form': form})

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

def drones_caracteristicas_list(request):
    drones_caracteristicas = DronesCaracteristicas.objects.all()
    return render(request, 'drones/drones_caracteristicas_list.html', {'drones_caracteristicas': drones_caracteristicas})

def drones_caracteristica_detail(request, pk):
    drone_caracteristica = DronesCaracteristicas.objects.get(pk=pk)
    return render(request, 'drones/drones_caracteristica_detail.html', {'drone_caracteristica': drone_caracteristica})

def drones_caracteristica_create(request):
    if request.method == 'POST':
        form = DronesCaracteristicasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drones_caracteristicas_list')
    else:
        form = DronesCaracteristicasForms()
    return render(request, 'drones/drones_caracteristica_form.html', {'form': form})

def drones_caracteristica_update(request, pk):
    drone_caracteristica = DronesCaracteristicas.objects.get(pk=pk)
    if request.method == 'POST':
        form = DronesCaracteristicasForms(request.POST, instance=drone_caracteristica)
        if form.is_valid():
            form.save()
            return redirect('drones_caracteristicas_list')
    else:
        form = DronesCaracteristicasForms(instance=drone_caracteristica)
    return render(request, 'drones/drones_caracteristica_form.html', {'form': form})

def drones_caracteristica_delete(request, pk):
    drone_caracteristica = DronesCaracteristicas.objects.get(pk=pk)
    if request.method == 'POST':
        drone_caracteristica.delete()
        return redirect('drones_caracteristicas_list')
    return render(request, 'drones/drones_caracteristica_confirm_delete.html', {'drone_caracteristica': drone_caracteristica})

########################
# End of CRUD Operations for DronesCaracteristicas Model
########################

########################
# CRUD Operations for EnergiaMarcas Model
########################

def energia_marcas_list(request):
    energia_marcas = EnergiaMarcas.objects.all()
    return render(request, 'energia/energia_marcas_list.html', {'energia_marcas': energia_marcas})

def energia_marca_detail(request, pk):
    energia_marca = EnergiaMarcas.objects.get(pk=pk)
    return render(request, 'energia/energia_marca_detail.html', {'energia_marca': energia_marca})

def energia_marca_create(request):
    if request.method == 'POST':
        form = EnergiaMarcasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('energia_marcas_list')
    else:
        form = EnergiaMarcasForms()
    return render(request, 'energia/energia_marca_form.html', {'form': form})

def energia_marca_update(request, pk):
    energia_marca = EnergiaMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = EnergiaMarcasForms(request.POST, instance=energia_marca)
        if form.is_valid():
            form.save()
            return redirect('energia_marcas_list')
    else:
        form = EnergiaMarcasForms(instance=energia_marca)
    return render(request, 'energia/energia_marca_form.html', {'form': form})

def energia_marca_delete(request, pk):
    energia_marca = EnergiaMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        energia_marca.delete()
        return redirect('energia_marcas_list')
    return render(request, 'energia/energia_marca_confirm_delete.html', {'energia_marca': energia_marca})

########################
# End of CRUD Operations for EnergiaMarcas Model
########################

########################
# CRUD Operations for Energias Model
########################

def energias_list(request):
    energias = Energias.objects.all()
    return render(request, 'energia/energias_list.html', {'energias': energias})

def energia_detail(request, pk):
    energia = Energias.objects.get(pk=pk)
    return render(request, 'energia/energia_detail.html', {'energia': energia})

def energia_create(request):
    if request.method == 'POST':
        form = EnergiasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('energias_list')
    else:
        form = EnergiasForms()
    return render(request, 'energia/energia_form.html', {'form': form})

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

def enlaces_list(request):
    enlaces = Enlaces.objects.all()
    return render(request, 'enlaces/enlaces_list.html', {'enlaces': enlaces})

def enlace_detail(request, pk):
    enlace = Enlaces.objects.get(pk=pk)
    return render(request, 'enlaces/enlace_detail.html', {'enlace': enlace})

def enlace_create(request):
    if request.method == 'POST':
        form = EnlacesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enlaces_list')
    else:
        form = EnlacesForms()
    return render(request, 'enlaces/enlace_form.html', {'form': form})

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

def enlaces_tipos_list(request):
    enlaces_tipos = EnlacesTipos.objects.all()
    return render(request, 'enlaces/enlaces_tipos_list.html', {'enlaces_tipos': enlaces_tipos})

def enlace_tipo_detail(request, pk):
    enlace_tipo = EnlacesTipos.objects.get(pk=pk)
    return render(request, 'enlaces/enlace_tipo_detail.html', {'enlace_tipo': enlace_tipo})

def enlace_tipo_create(request):
    if request.method == 'POST':
        form = EnlacesTiposForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enlaces_tipos_list')
    else:
        form = EnlacesTiposForms()
    return render(request, 'enlaces/enlace_tipo_form.html', {'form': form})

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

def equipo_telefonico_list(request):
    equipo_telefonico = EquipoTelefonico.objects.all()
    return render(request, 'equipos/equipo_telefonico_list.html', {'equipo_telefonico': equipo_telefonico})

def equipo_telefonico_detail(request, pk):
    equipo = EquipoTelefonico.objects.get(pk=pk)
    return render(request, 'equipos/equipo_telefonico_detail.html', {'equipo': equipo})

def equipo_telefonico_create(request):
    if request.method == 'POST':
        form = EquipoTelefonicoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipo_telefonico_list')
    else:
        form = EquipoTelefonicoForms()
    return render(request, 'equipos/equipo_telefonico_form.html', {'form': form})

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

def equipos_personales_list(request):
    equipos_personales = EquiposPersonales.objects.all()
    return render(request, 'equipos/equipos_personales_list.html', {'equipos_personales': equipos_personales})

def equipo_personal_detail(request, pk):
    equipo_personal = EquiposPersonales.objects.get(pk=pk)
    return render(request, 'equipos/equipo_personal_detail.html', {'equipo_personal': equipo_personal})

def equipo_personal_create(request):
    if request.method == 'POST':
        form = EquiposPersonalesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_personales_list')
    else:
        form = EquiposPersonalesForms()
    return render(request, 'equipos/equipo_personal_form.html', {'form': form})

def equipo_personal_update(request, pk):
    equipo_personal = EquiposPersonales.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposPersonalesForms(request.POST, instance=equipo_personal)
        if form.is_valid():
            form.save()
            return redirect('equipos_personales_list')
    else:
        form = EquiposPersonalesForms(instance=equipo_personal)
    return render(request, 'equipos/equipo_personal_form.html', {'form': form})

def equipo_personal_delete(request, pk):
    equipo_personal = EquiposPersonales.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_personal.delete()
        return redirect('equipos_personales_list')
    return render(request, 'equipos/equipo_personal_confirm_delete.html', {'equipo_personal': equipo_personal})

########################
# End of CRUD Operations for EquiposPersonales Model
########################

########################
# CRUD Operations for EquiposPersonalesMarcas Model
########################

def equipos_personales_marcas_list(request):
    equipos_personales_marcas = EquiposPersonalesMarcas.objects.all()
    return render(request, 'equipos/equipos_personales_marcas_list.html', {'equipos_personales_marcas': equipos_personales_marcas})

def equipo_personal_marca_detail(request, pk):
    equipo_personal_marca = EquiposPersonalesMarcas.objects.get(pk=pk)
    return render(request, 'equipos/equipo_personal_marca_detail.html', {'equipo_personal_marca': equipo_personal_marca})

def equipo_personal_marca_create(request):
    if request.method == 'POST':
        form = EquiposPersonalesMarcasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_personales_marcas_list')
    else:
        form = EquiposPersonalesMarcasForms()
    return render(request, 'equipos/equipo_personal_marca_form.html', {'form': form})

def equipo_personal_marca_update(request, pk):
    equipo_personal_marca = EquiposPersonalesMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposPersonalesMarcasForms(request.POST, instance=equipo_personal_marca)
        if form.is_valid():
            form.save()
            return redirect('equipos_personales_marcas_list')
    else:
        form = EquiposPersonalesMarcasForms(instance=equipo_personal_marca)
    return render(request, 'equipos/equipo_personal_marca_form.html', {'form': form})

def equipo_personal_marca_delete(request, pk):
    equipo_personal_marca = EquiposPersonalesMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_personal_marca.delete()
        return redirect('equipos_personales_marcas_list')
    return render(request, 'equipos/equipo_personal_marca_confirm_delete.html', {'equipo_personal_marca': equipo_personal_marca})

########################
# End of CRUD Operations for EquiposPersonalesMarcas Model
########################

########################
# CRUD Operations for EquiposServidores Model
########################

def equipos_servidores_list(request):
    equipos_servidores = EquiposServidores.objects.all()
    return render(request, 'equipos/equipos_servidores_list.html', {'equipos_servidores': equipos_servidores})

def equipo_servidor_detail(request, pk):
    equipo_servidor = EquiposServidores.objects.get(pk=pk)
    return render(request, 'equipos/equipo_servidor_detail.html', {'equipo_servidor': equipo_servidor})

def equipo_servidor_create(request):
    if request.method == 'POST':
        form = EquiposServidoresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_list')
    else:
        form = EquiposServidoresForms()
    return render(request, 'equipos/equipo_servidor_form.html', {'form': form})

def equipo_servidor_update(request, pk):
    equipo_servidor = EquiposServidores.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposServidoresForms(request.POST, instance=equipo_servidor)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_list')
    else:
        form = EquiposServidoresForms(instance=equipo_servidor)
    return render(request, 'equipos/equipo_servidor_form.html', {'form': form})

def equipo_servidor_delete(request, pk):
    equipo_servidor = EquiposServidores.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_servidor.delete()
        return redirect('equipos_servidores_list')
    return render(request, 'equipos/equipo_servidor_confirm_delete.html', {'equipo_servidor': equipo_servidor})

########################
# End of CRUD Operations for EquiposServidores Model
########################

########################
# CRUD Operations for EquiposServidoresMarcas Model
########################

def equipos_servidores_marcas_list(request):
    equipos_servidores_marcas = EquiposServidoresMarcas.objects.all()
    return render(request, 'equipos/equipos_servidores_marcas_list.html', {'equipos_servidores_marcas': equipos_servidores_marcas})

def equipo_servidor_marca_detail(request, pk):
    equipo_servidor_marca = EquiposServidoresMarcas.objects.get(pk=pk)
    return render(request, 'equipos/equipo_servidor_marca_detail.html', {'equipo_servidor_marca': equipo_servidor_marca})

def equipo_servidor_marca_create(request):
    if request.method == 'POST':
        form = EquiposServidoresMarcasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_marcas_list')
    else:
        form = EquiposServidoresMarcasForms()
    return render(request, 'equipos/equipo_servidor_marca_form.html', {'form': form})

def equipo_servidor_marca_update(request, pk):
    equipo_servidor_marca = EquiposServidoresMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposServidoresMarcasForms(request.POST, instance=equipo_servidor_marca)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_marcas_list')
    else:
        form = EquiposServidoresMarcasForms(instance=equipo_servidor_marca)
    return render(request, 'equipos/equipo_servidor_marca_form.html', {'form': form})

def equipo_servidor_marca_delete(request, pk):
    equipo_servidor_marca = EquiposServidoresMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_servidor_marca.delete()
        return redirect('equipos_servidores_marcas_list')
    return render(request, 'equipos/equipo_servidor_marca_confirm_delete.html', {'equipo_servidor_marca': equipo_servidor_marca})

########################
# End of CRUD Operations for EquiposServidoresMarcas Model
########################

########################
# CRUD Operations for EquiposServidoresProcesadores Model
########################

def equipos_servidores_procesadores_list(request):
    equipos_servidores_procesadores = EquiposServidoresProcesadores.objects.all()
    return render(request, 'equipos/equipos_servidores_procesadores_list.html', {'equipos_servidores_procesadores': equipos_servidores_procesadores})

def equipo_servidor_procesador_detail(request, pk):
    equipo_servidor_procesador = EquiposServidoresProcesadores.objects.get(pk=pk)
    return render(request, 'equipos/equipo_servidor_procesador_detail.html', {'equipo_servidor_procesador': equipo_servidor_procesador})

def equipo_servidor_procesador_create(request):
    if request.method == 'POST':
        form = EquiposServidoresProcesadoresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_procesadores_list')
    else:
        form = EquiposServidoresProcesadoresForms()
    return render(request, 'equipos/equipo_servidor_procesador_form.html', {'form': form})

def equipo_servidor_procesador_update(request, pk):
    equipo_servidor_procesador = EquiposServidoresProcesadores.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposServidoresProcesadoresForms(request.POST, instance=equipo_servidor_procesador)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_procesadores_list')
    else:
        form = EquiposServidoresProcesadoresForms(instance=equipo_servidor_procesador)
    return render(request, 'equipos/equipo_servidor_procesador_form.html', {'form': form})

def equipo_servidor_procesador_delete(request, pk):
    equipo_servidor_procesador = EquiposServidoresProcesadores.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_servidor_procesador.delete()
        return redirect('equipos_servidores_procesadores_list')
    return render(request, 'equipos/equipo_servidor_procesador_confirm_delete.html', {'equipo_servidor_procesador': equipo_servidor_procesador})

########################
# End of CRUD Operations for EquiposServidoresProcesadores Model
########################

########################
# CRUD Operations for EquiposServidoresTipos Model
########################

def equipos_servidores_tipos_list(request):
    equipos_servidores_tipos = EquiposServidoresTipos.objects.all()
    return render(request, 'equipos/equipos_servidores_tipos_list.html', {'equipos_servidores_tipos': equipos_servidores_tipos})

def equipo_servidor_tipo_detail(request, pk):
    equipo_servidor_tipo = EquiposServidoresTipos.objects.get(pk=pk)
    return render(request, 'equipos/equipo_servidor_tipo_detail.html', {'equipo_servidor_tipo': equipo_servidor_tipo})

def equipo_servidor_tipo_create(request):
    if request.method == 'POST':
        form = EquiposServidoresTiposForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_tipos_list')
    else:
        form = EquiposServidoresTiposForms()
    return render(request, 'equipos/equipo_servidor_tipo_form.html', {'form': form})

def equipo_servidor_tipo_update(request, pk):
    equipo_servidor_tipo = EquiposServidoresTipos.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquiposServidoresTiposForms(request.POST, instance=equipo_servidor_tipo)
        if form.is_valid():
            form.save()
            return redirect('equipos_servidores_tipos_list')
    else:
        form = EquiposServidoresTiposForms(instance=equipo_servidor_tipo)
    return render(request, 'equipos/equipo_servidor_tipo_form.html', {'form': form})

def equipo_servidor_tipo_delete(request, pk):
    equipo_servidor_tipo = EquiposServidoresTipos.objects.get(pk=pk)
    if request.method == 'POST':
        equipo_servidor_tipo.delete()
        return redirect('equipos_servidores_tipos_list')
    return render(request, 'equipos/equipo_servidor_tipo_confirm_delete.html', {'equipo_servidor_tipo': equipo_servidor_tipo})

########################
# End of CRUD Operations for EquiposServidoresTipos Model
########################

########################
# CRUD Operations for Firewalls Model
########################

def firewalls_list(request):
    firewalls = Firewalls.objects.all()
    return render(request, 'firewalls/firewalls_list.html', {'firewalls': firewalls})

def firewall_detail(request, pk):
    firewall = Firewalls.objects.get(pk=pk)
    return render(request, 'firewalls/firewall_detail.html', {'firewall': firewall})

def firewall_create(request):
    if request.method == 'POST':
        form = FirewallsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('firewalls_list')
    else:
        form = FirewallsForms()
    return render(request, 'firewalls/firewall_form.html', {'form': form})

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

def firewalls_marcas_list(request):
    firewalls_marcas = FirewallsMarcas.objects.all()
    return render(request, 'firewalls/firewalls_marcas_list.html', {'firewalls_marcas': firewalls_marcas})

def firewall_marca_detail(request, pk):
    firewall_marca = FirewallsMarcas.objects.get(pk=pk)
    return render(request, 'firewalls/firewall_marca_detail.html', {'firewall_marca': firewall_marca})

def firewall_marca_create(request):
    if request.method == 'POST':
        form = FirewallsMarcasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('firewalls_marcas_list')
    else:
        form = FirewallsMarcasForms()
    return render(request, 'firewalls/firewall_marca_form.html', {'form': form})

def firewall_marca_update(request, pk):
    firewall_marca = FirewallsMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = FirewallsMarcasForms(request.POST, instance=firewall_marca)
        if form.is_valid():
            form.save()
            return redirect('firewalls_marcas_list')
    else:
        form = FirewallsMarcasForms(instance=firewall_marca)
    return render(request, 'firewalls/firewall_marca_form.html', {'form': form})

def firewall_marca_delete(request, pk):
    firewall_marca = FirewallsMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        firewall_marca.delete()
        return redirect('firewalls_marcas_list')
    return render(request, 'firewalls/firewall_marca_confirm_delete.html', {'firewall_marca': firewall_marca})

########################
# End of CRUD Operations for FirewallsMarcas Model
########################

########################
# CRUD Operations for HerramientaDeDesarrollo Model
########################

def herramientas_desarrollo_list(request):
    herramientas_desarrollo = HerramientaDeDesarrollo.objects.all()
    return render(request, 'herramientas/herramientas_desarrollo_list.html', {'herramientas_desarrollo': herramientas_desarrollo})

def herramienta_desarrollo_detail(request, pk):
    herramienta_desarrollo = HerramientaDeDesarrollo.objects.get(pk=pk)
    return render(request, 'herramientas/herramienta_desarrollo_detail.html', {'herramienta_desarrollo': herramienta_desarrollo})

def herramienta_desarrollo_create(request):
    if request.method == 'POST':
        form = HerramientaDeDesarrolloForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('herramientas_desarrollo_list')
    else:
        form = HerramientaDeDesarrolloForms()
    return render(request, 'herramientas/herramienta_desarrollo_form.html', {'form': form})

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

def impresoras_list(request):
    impresoras = Impresoras.objects.all()
    return render(request, 'impresoras/impresoras_list.html', {'impresoras': impresoras})

def impresora_detail(request, pk):
    impresora = Impresoras.objects.get(pk=pk)
    return render(request, 'impresoras/impresora_detail.html', {'impresora': impresora})

def impresora_create(request):
    if request.method == 'POST':
        form = ImpresorasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('impresoras_list')
    else:
        form = ImpresorasForms()
    return render(request, 'impresoras/impresora_form.html', {'form': form})

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

def impresoras_marcas_list(request):
    impresoras_marcas = ImpresorasMarcas.objects.all()
    return render(request, 'impresoras/impresoras_marcas_list.html', {'impresoras_marcas': impresoras_marcas})

def impresora_marca_detail(request, pk):
    impresora_marca = ImpresorasMarcas.objects.get(pk=pk)
    return render(request, 'impresoras/impresora_marca_detail.html', {'impresora_marca': impresora_marca})

def impresora_marca_create(request):
    if request.method == 'POST':
        form = ImpresorasMarcasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('impresoras_marcas_list')
    else:
        form = ImpresorasMarcasForms()
    return render(request, 'impresoras/impresora_marca_form.html', {'form': form})

def impresora_marca_update(request, pk):
    impresora_marca = ImpresorasMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImpresorasMarcasForms(request.POST, instance=impresora_marca)
        if form.is_valid():
            form.save()
            return redirect('impresoras_marcas_list')
    else:
        form = ImpresorasMarcasForms(instance=impresora_marca)
    return render(request, 'impresoras/impresora_marca_form.html', {'form': form})

def impresora_marca_delete(request, pk):
    impresora_marca = ImpresorasMarcas.objects.get(pk=pk)
    if request.method == 'POST':
        impresora_marca.delete()
        return redirect('impresoras_marcas_list')
    return render(request, 'impresoras/impresora_marca_confirm_delete.html', {'impresora_marca': impresora_marca})

########################
# End of CRUD Operations for ImpresorasMarcas Model
########################

########################
# CRUD Operations for Proyectores Model
########################

def proyectores_list(request):
    proyectores = Proyectores.objects.all()
    return render(request, 'proyectores/proyectores_list.html', {'proyectores': proyectores})

def proyector_detail(request, pk):
    proyector = Proyectores.objects.get(pk=pk)
    return render(request, 'proyectores/proyector_detail.html', {'proyector': proyector})

def proyector_create(request):
    if request.method == 'POST':
        form = ProyectoresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyectores_list')
    else:
        form = ProyectoresForms()
    return render(request, 'proyectores/proyector_form.html', {'form': form})

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
# CRUD Operations for Routers Model
########################

def routers_list(request):
    routers = Routers.objects.all()
    return render(request, 'routers/routers_list.html', {'routers': routers})

def router_detail(request, pk):
    router = Routers.objects.get(pk=pk)
    return render(request, 'routers/router_detail.html', {'router': router})

def router_create(request):
    if request.method == 'POST':
        form = RoutersForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('routers_list')
    else:
        form = RoutersForms()
    return render(request, 'routers/router_form.html', {'form': form})

def router_update(request, pk):
    router = Routers.objects.get(pk=pk)
    if request.method == 'POST':
        form = RoutersForms(request.POST, instance=router)
        if form.is_valid():
            form.save()
            return redirect('routers_list')
    else:
        form = RoutersForms(instance=router)
    return render(request, 'routers/router_form.html', {'form': form})

def router_delete(request, pk):
    router = Routers.objects.get(pk=pk)
    if request.method == 'POST':
        router.delete()
        return redirect('routers_list')
    return render(request, 'routers/router_confirm_delete.html', {'router': router})

########################
# End of CRUD Operations for Routers Model
########################

########################
# CRUD Operations for Secretarias Model
########################

def secretarias_list(request):
    secretarias = Secretarias.objects.all()
    return render(request, 'secretarias/secretarias_list.html', {'secretarias': secretarias})

def secretaria_detail(request, pk):
    secretaria = Secretarias.objects.get(pk=pk)
    return render(request, 'secretarias/secretaria_detail.html', {'secretaria': secretaria})

def secretaria_create(request):
    if request.method == 'POST':
        form = SecretariasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secretarias_list')
    else:
        form = SecretariasForms()
    return render(request, 'secretarias/secretaria_form.html', {'form': form})

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
# CRUD Operations for SistemaDeInformacionMovil Model
########################

def sistemas_informacion_movil_list(request):
    sistemas_informacion_movil = SistemaDeInformacionMovil.objects.all()
    return render(request, 'sistemas_informacion_movil/sistemas_informacion_movil_list.html', {'sistemas_informacion_movil': sistemas_informacion_movil})

def sistema_informacion_movil_detail(request, pk):
    sistema_informacion_movil = SistemaDeInformacionMovil.objects.get(pk=pk)
    return render(request, 'sistemas_informacion_movil/sistema_informacion_movil_detail.html', {'sistema_informacion_movil': sistema_informacion_movil})

def sistema_informacion_movil_create(request):
    if request.method == 'POST':
        form = SistemaDeInformacionMovilForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistemas_informacion_movil_list')
    else:
        form = SistemaDeInformacionMovilForms()
    return render(request, 'sistemas_informacion_movil/sistema_informacion_movil_form.html', {'form': form})

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

def sistemas_informacion_movil_nombres_list(request):
    sistemas_informacion_movil_nombres = SistemaInformacionMovilNombres.objects.all()
    return render(request, 'sistema_informacion_movil_nombres/sistemas_informacion_movil_nombres_list.html', {'sistemas_informacion_movil_nombres': sistemas_informacion_movil_nombres})

def sistema_informacion_movil_nombre_detail(request, pk):
    sistema_informacion_movil_nombre = SistemaInformacionMovilNombres.objects.get(pk=pk)
    return render(request, 'sistema_informacion_movil_nombres/sistema_informacion_movil_nombre_detail.html', {'sistema_informacion_movil_nombre': sistema_informacion_movil_nombre})

def sistema_informacion_movil_nombre_create(request):
    if request.method == 'POST':
        form = SistemaInformacionMovilNombresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistemas_informacion_movil_nombres_list')
    else:
        form = SistemaInformacionMovilNombresForms()
    return render(request, 'sistema_informacion_movil_nombres/sistema_informacion_movil_nombre_form.html', {'form': form})

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

def sistemas_informacion_list(request):
    sistemas_informacion = SistemasInformacion.objects.all()
    return render(request, 'sistemas_informacion/sistemas_informacion_list.html', {'sistemas_informacion': sistemas_informacion})

def sistema_informacion_detail(request, pk):
    sistema_informacion = SistemasInformacion.objects.get(pk=pk)
    return render(request, 'sistemas_informacion/sistema_informacion_detail.html', {'sistema_informacion': sistema_informacion})

def sistema_informacion_create(request):
    if request.method == 'POST':
        form = SistemasInformacionForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistemas_informacion_list')
    else:
        form = SistemasInformacionForms()
    return render(request, 'sistemas_informacion/sistema_informacion_form.html', {'form': form})

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

def sistemas_informacion_nombres_list(request):
    sistemas_informacion_nombres = SistemasInformacionNombres.objects.all()
    return render(request, 'sistemas_informacion_nombres/sistemas_informacion_nombres_list.html', {'sistemas_informacion_nombres': sistemas_informacion_nombres})

def sistema_informacion_nombre_detail(request, pk):
    sistema_informacion_nombre = SistemasInformacionNombres.objects.get(pk=pk)
    return render(request, 'sistemas_informacion_nombres/sistema_informacion_nombre_detail.html', {'sistema_informacion_nombre': sistema_informacion_nombre})

def sistema_informacion_nombre_create(request):
    if request.method == 'POST':
        form = SistemasInformacionNombresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistemas_informacion_nombres_list')
    else:
        form = SistemasInformacionNombresForms()
    return render(request, 'sistemas_informacion_nombres/sistema_informacion_nombre_form.html', {'form': form})

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

def sites_list(request):
    sites = Sites.objects.all()
    return render(request, 'sites/sites_list.html', {'sites': sites})

def site_detail(request, pk):
    site = Sites.objects.get(pk=pk)
    return render(request, 'sites/site_detail.html', {'site': site})

def site_create(request):
    if request.method == 'POST':
        form = SitesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sites_list')
    else:
        form = SitesForms()
    return render(request, 'sites/site_form.html', {'form': form})

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

def usuarios_list(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuarios/usuarios_list.html', {'usuarios': usuarios})

def usuario_detail(request, pk):
    usuario = Usuarios.objects.get(pk=pk)
    return render(request, 'usuarios/usuario_detail.html', {'usuario': usuario})

def usuario_create(request):
    if request.method == 'POST':
        form = UsuariosForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios_list')
    else:
        form = UsuariosForms()
    return render(request, 'usuarios/usuario_form.html', {'form': form})

def usuario_update(request, pk):
    usuario = Usuarios.objects.get(pk=pk)
    if request.method == 'POST':
        form = UsuariosForms(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios_list')
    else:
        form = UsuariosForms(instance=usuario)
    return render(request, 'usuarios/usuario_form.html', {'form': form})

def usuario_delete(request, pk):
    usuario = Usuarios.objects.get(pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios_list')
    return render(request, 'usuarios/usuario_confirm_delete.html', {'usuario': usuario})

########################
# End of CRUD Operations for Usuarios Model
########################
