from django.shortcuts import render, redirect
from .conmutadores_views import *
from django.urls import reverse 
from ..models import *
import pandas as pd

def carga(request):
    secretarias = Secretarias.objects.all()
    dependencias = Dependencias.objects.all()
    #<QueryDict: {'categoria': ['201'], 'subcategoriaSelec': ['1050'], 'dependenciaSelec': ['517'], 'year': ['']}>
    if request.method == 'POST'  and 'ex' in request.FILES:
        selected_secretaria = request.POST.get('secretaria')
        archivo_excel = request.FILES.get('ex')
        subcategoria_seleccionada = request.POST.get('subcategoriaSelec')
        anio = request.POST.get('year')
        dependencia = request.POST.get('dependenciaSelec')
        print(request.POST)
        if not(archivo_excel and subcategoria_seleccionada and anio and dependencia):
            return render(request, "carga.html", {
               'secretarias': secretarias,
               'dependencias': dependencias,
               'selected_secretaria': request.POST.get('secretaria')
            })
        try:
            df = pd.read_excel(archivo_excel)
            cabeceras = df.columns.tolist()
            datos = df.values.tolist()

        except Exception as e:
            print(e)
            return render(request, "carga.html", {
               'secretarias': secretarias,
               'dependencias': dependencias,
               'selected_secretaria': request.POST.get('secretaria')
            })
        
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)

        msj, exito = "Nulo", False

        if subcategoria_seleccionada == "1092":
            msj,exito = carga_conmutadores(df,anio,dependencia)
        if subcategoria_seleccionada == "1010":
            return redirect(reverse('energias_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1020":
            return redirect(reverse('almacenamientos_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1030":
            return redirect(reverse('equipos_personales_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1040":
            return redirect(reverse('equipos_servidores_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1050":
            return redirect(reverse('impresoras_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1060":
            return redirect(reverse('proyectores_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1080":
            return redirect(reverse('drones_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1090":
            return redirect(reverse('firewalls_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1091":
            return redirect(reverse('routers_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1110":
            return redirect(reverse('herramientas_desarrollo_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1120":
            return redirect(reverse('sistemas_informacion_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1130":
            return redirect(reverse('sistemas_informacion_movil_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1210":
            return redirect(reverse('enlaces_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1230":
            return redirect(reverse('sites_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)
        
        if subcategoria_seleccionada == "1310":
            return redirect(reverse('sites_list') + '?dependencia='+dependencia+'&anio='+year+'&search='+serch)

        return render(request, 'carga.html', {
            'cabeceras': cabeceras,
            'datos': datos,
            'secretarias': secretarias,
            'dependencias': dependencias,
            'selected_secretaria': selected_secretaria,
            'msj':msj,
            'exito':exito
        })
    

    return render(request, "carga.html", {
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.POST.get('secretaria')
    })

def carga_conmutadores(df,anio,dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            tipo = row.get('Tipo', None)
            tecnologia = row.get('Tecnologia', None)
            protocolo = row.get('Protocolo', None)
            ext_soportadas = row.get('Ext_soportadas', None)
            modelo = row.get('Modelo', None)
            marca_nombre = row.get('Marca', None)
            
            # Buscar la dependencia y la marca en la base de datos
            marca = ConmutadoresMarcas.objects.get(marca_conmutador=marca_nombre)
            
            conmutador = Conmutadores(
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_dependencia=dependencia,
                tipo=tipo,
                tecnologia=tecnologia,
                protocolo=protocolo,
                ext_soportadas=ext_soportadas,
                modelo=modelo,
                id_marca=marca
            )
            # Guardar el conmutador en la base de datos
            conmutador.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}",False
    else:
        return "Conmutadores cargados exitosamente",True
