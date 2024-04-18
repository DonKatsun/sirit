from django.shortcuts import render, redirect
from ..models import Conmutadores, ConmutadoresMarcas
from ..forms import ConmutadorForm, ConmutadorMarcaForm

def conmutadores_list(request, *args, **kwargs):
    conmutadores = Conmutadores.objects.all()
    return render(request, 'conmutadores/conmutadores_list.html', {'conmutadores': conmutadores})



def conmutador_detail(request, pk):
    conmutador = Conmutadores.objects.get(pk=pk)
    return render(request, 'conmutadores/conmutador_detail.html', {'conmutador': conmutador})

def conmutador_create(request):
    if request.method == 'POST':
        form = ConmutadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conmutadores_list')
    else:
        form = ConmutadorForm()
    return render(request, 'conmutadores/conmutador_form.html', {'form': form})

def conmutador_update(request, pk):
    conmutador = Conmutadores.objects.get(pk=pk)
    if request.method == 'POST':
        form = ConmutadorForm(request.POST, instance=conmutador)
        if form.is_valid():
            form.save()
            return redirect('conmutadores_list')
    else:
        form = ConmutadorForm(instance=conmutador)
    return render(request, 'conmutadores/conmutador_form.html', {'form': form})

def conmutador_delete(request, pk):
    conmutador = Conmutadores.objects.get(pk=pk)
    if request.method == 'POST':
        conmutador.delete()
        return redirect('conmutadores_list')
    return render(request, 'conmutadores/conmutador_confirm_delete.html', {'conmutador': conmutador})

