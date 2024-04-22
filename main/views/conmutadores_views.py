from django.shortcuts import render, redirect
from ..models import Conmutadores, ConmutadoresMarcas,Dependencias, Secretarias
from ..forms import ConmutadorForm, ConmutadorMarcaForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def conmutadores_list(request, *args, **kwargs):
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    year = request.GET.get('anio')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
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
    
    if search:
        conmutadores = conmutadores.filter(no_inventario__icontains=search)
    paginator = Paginator(conmutadores, 10)  # Muestra 10 conmutadores por página

    page_number = request.GET.get('page')
    try:
        conmutadores = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, muestra la primera página.
        conmutadores = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango (por encima del número total de páginas), muestra la última página.
        conmutadores = paginator.page(paginator.num_pages)
    
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

