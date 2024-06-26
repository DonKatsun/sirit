from django.shortcuts import render, redirect
from ..models import *
from ..forms import ConmutadorForm, ConmutadorMarcaForm
from django.apps import apps


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import openpyxl
from django.http import HttpResponse
def usu(request):
    user_id = request.user.id
    usuario = (Usuarios.objects.get(usuario=user_id))
    rol=(usuario.id_rol.id)
    return rol

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


@login_required
def conmutadores_list(request, *args, **kwargs):
    secretarias = Secretarias.objects.all().order_by('nombre_secretaria')
    dependencias = Dependencias.objects.all().order_by('nombre_dependencia')
    year = request.GET.get('anio')
    secretaria = request.GET.get('secretariaSelec')
    dependencia = request.GET.get('dependencia')
    search = request.GET.get('search')
    categoria = request.GET.get('categoria')
    print("Categoria: "+categoria)
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
    
    if secretaria:
        conmutadores = conmutadores.filter(id_dependencia__id_secretaria=secretaria)
    if search:
        conmutadores = conmutadores.filter(no_inventario__icontains=search)
    
    if request.GET.get('descarga') == '1':
        return generate_excel('conmutadores', conmutadores)
    
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
    rol = usu(request)

    if rol != 1:
         return render(request, 'conmutadores/conmutadores_list.html', {
        'conmutadores': conmutadores,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'nav': "1",
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'inventario': 'Conmutador',
        'clave': '1092',
        'categoria_seleccionada':categoria if categoria else '',
    })
    return render(request, 'conmutadores/conmutadores_list.html', {
        'conmutadores': conmutadores,
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.GET.get('secretaria'),
        'anio':year,
        'secretaria': None if not secretaria else Secretarias.objects.filter(id=secretaria).first(),
        'dependencia': None if not dependencia else Dependencias.objects.filter(id=dependencia).first(),
        'inventario': 'Conmutador',
        'clave': '1092',
        'categoria_seleccionada':categoria if categoria else '',
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

