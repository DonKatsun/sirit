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


                                                                    ######    ######
                                                                  ########## ##########
                                                                #########################
                                                                #########################
                                                                ########################
                                                                 ######################
                                                                   ##################
                                                                     ##############
                                                                       ##########
                                                                         ######
                                                                           ##

#              /\_/\  
#     _______/ o o \ 
#    /         \ Y / 
#   |   \     / - \  
#   |  ||   |        
#   |  ~~   ~~        
#   \__|         |
#      \ _______/ 