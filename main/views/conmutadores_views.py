from django.shortcuts import render, redirect
from ..models import Conmutadores, ConmutadoresMarcas,Dependencias, Secretarias
from ..forms import ConmutadorForm, ConmutadorMarcaForm

def conmutadores_list(request, *args, **kwargs):
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    dependencia = request.GET.get('dependencia')
    if 'secretaria' in request.GET:
        selected_secretaria = request.GET['secretaria']
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)
    if year:
        if dependencia:
            conmutadores = Conmutadores.objects.filter(id_dependencia=dependencia,fecha__year=year)
        else:
            conmutadores = Conmutadores.objects.filter(fecha__year=year)
    else:
        conmutadores = Conmutadores.objects.all()
    print(conmutadores)
    return render(request, 'conmutadores/conmutadores_list.html', {
        'conmutadores': conmutadores,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria')
        })



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

