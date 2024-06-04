from django.shortcuts import render, redirect
from .conmutadores_views import *
from django.urls import reverse 
from ..models import *
import pandas as pd
from django.contrib.auth.decorators import login_required
@login_required
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
               'selected_secretaria': request.POST.get('secretaria'),
               
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
               'selected_secretaria': request.POST.get('secretaria'),
               
            })
        
        if selected_secretaria:
            dependencias = Dependencias.objects.filter(id_secretaria=selected_secretaria)

        msj, exito = "Nulo", False

        if subcategoria_seleccionada == "1092":
            msj,exito = carga_conmutadores(df,anio,dependencia)

        if subcategoria_seleccionada == "1010":
            msj,exito = carga_energias(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1020":
            msj,exito = carga_almacenamientos(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1030":
            msj,exito = carga_equipos_personales(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1040":
            msj,exito = carga_equipos_servidores(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1050":
            msj,exito = carga_impresoras(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1060":
            msj,exito = carga_proyectores(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1080":
            msj,exito = carga_drones(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1090":
            msj,exito = carga_firewalls(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1091":
            msj,exito = carga_routers(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1110":
            msj,exito = carga_herramientas_desarrollo(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1120":
            msj,exito = carga_sistemas_informacion(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1130":
            msj,exito = carga_sistemas_informacion_movil(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1210":
            msj,exito = carga_enlaces(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1230":
            msj,exito = carga_sites(df,anio,dependencia)
        
        if subcategoria_seleccionada == "1310":
            return redirect(reverse('principal'))

        return render(request, 'carga.html', {
            'cabeceras': cabeceras,
            'datos': datos,
            'secretarias': secretarias,
            'dependencias': dependencias,
            'selected_secretaria': selected_secretaria,
            'msj':msj,
            'exito':exito,
            
        })
    
    elif request.method == 'POST':
       return render(request, "carga.html", {
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.POST.get('secretaria'),
        'error_message': 'Ningún archivo seleccionado'
    }) 

    return render(request, "carga.html", {
        'secretarias': secretarias,
        'dependencias': dependencias,
        'selected_secretaria': request.POST.get('secretaria'),
        
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


def carga_energias(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            tipo = row.get('Tipo', None)
            capacidad = row.get('Capacidad', None)
            modelo = row.get('Modelo', None)
            marca_nombre = row.get('Marca', None)
            
            # Buscar la marca en la base de datos
            marca = EnergiaMarcas.objects.get(marca_energia=marca_nombre)
            
            # Crear una instancia de Energias con los datos de la fila
            energia = Energias(
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_dependencia=dependencia,
                capacidad=capacidad,
                tipo=tipo,
                modelo=modelo,
                id_marca=marca
            )
            # Guardar la energía en la base de datos
            energia.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Energías cargadas exitosamente", True

def carga_almacenamientos(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            tipo = row.get('Tipo', None)
            capacidad = row.get('Capacidad', None)
            marca_nombre = row.get('Marca', None)
            
            # Buscar la marca en la base de datos
            marca = AlmacenamientoMarcas.objects.get(marca_almacenamiento=marca_nombre)
            
            # Crear una instancia de Almacenamientos con los datos de la fila
            almacenamiento = Almacenamientos(
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_dependencia=dependencia,
                capacidad=capacidad,
                tipo=tipo,
                id_marca=marca
            )
            # Guardar el almacenamiento en la base de datos
            almacenamiento.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Almacenamientos cargados exitosamente", True

def carga_equipos_personales(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            tipo = row.get('Tipo', None)
            modelo = row.get('Modelo', None)
            velocidad_procesador = row.get('Velocidad_Procesador', None)
            ram = row.get('Ram', None)
            so = row.get('SO', None)
            almacenamiento = row.get('Almacenamiento', None)
            cantidad_puertos = row.get('puertos_USB', None)
            capacidad_disco = row.get('Capacidad_Disco', None)
            arquitectura = row.get('Arquitectura', None)
            licencia = row.get('Licencia', None)
            resolucion = row.get('Monitor', None)
            tipo_pantalla = row.get('Tipo_Pantalla', None)
            conexion_pantalla = row.get('Conexión', None)
            tamano = row.get('Monitor', None)
            marca_nombre = row.get('Marca', None)
            mac_alambrica = row.get('MAC', None)
            
            # Buscar la marca en la base de datos
            marca = EquiposPersonalesMarcas.objects.get(marca_equipopersonal=marca_nombre)
            
            # Crear una instancia de EquiposPersonales con los datos de la fila
            equipo_personal = EquiposPersonales(
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_dependencia=dependencia,
                tipo=tipo,
                modelo=modelo,
                velocidad_procesador=velocidad_procesador,
                ram=ram,
                so=so,
                almacenamiento=almacenamiento,
                cantidad_puertos=cantidad_puertos,
                capacidad_disco=capacidad_disco,
                arquitectura=arquitectura,
                licencia=licencia,
                resolucion=resolucion,
                tipo_pantalla=tipo_pantalla,
                conexion_pantalla=conexion_pantalla,
                tamano=tamano,
                id_marca=marca,
                mac_alambrica=mac_alambrica,
                mac_inalambrica=''  # Agrega un valor por defecto para evitar errores si la columna está vacía
            )
            # Guardar el equipo personal en la base de datos
            equipo_personal.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Equipos personales cargados exitosamente", True

def carga_equipos_servidores(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            tipo = row.get('Tipo', None)
            criticidad = row.get('Criticidad', None)
            proposito = row.get('Proposito_Servidor', None)
            velocidad = row.get('Velocidad_Procesador', None)
            ram = row.get('RAM_Maxima', None)
            opc = row.get('Licencia_SO', None)
            almacenamiento = row.get('Almacenamiento_Servidor', None)
            periodo_respaldo = row.get('Periodicidad_Respaldos', None)
            cantidad_nucleos = row.get('Numero_Nucleos', None)
            config_disco = row.get('Configuracion_Discos', None)
            software = row.get('Software_Servidor', None)
            ip_interna = row.get('ip_interna', None)
            ip_externa = row.get('ip_externa', None)
            no_serie = row.get('n_serie', None)
            licencia_so = row.get('Licencia_SO', None)
            tipo_respaldo = row.get('Tipo_Respaldo', None)
            marca_nombre = row.get('Servidor_Marca', None)
            modelo = row.get('Servidor_Modelo', None)

            # Buscar la marca en la base de datos
            marca = EquiposServidoresMarcas.objects.get(marca_equipopersonal=marca_nombre)

            # Buscar el tipo de servidor en la base de datos
            tipo_servidor_nombre = row.get('Tipo', None)
            tipo_servidor = EquiposServidoresTipos.objects.get(tipo_equipopersonal=tipo_servidor_nombre)
            
            # Crear una instancia de EquiposServidores con los datos de la fila
            equipo_servidor = EquiposServidores(
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_dependencia=dependencia,
                tipo=tipo,
                criticidad=criticidad,
                proposito=proposito,
                velocidad=velocidad,
                ram=ram,
                opc=opc,
                almacenamiento=almacenamiento,
                periodo_respaldo=periodo_respaldo,
                cantidad_nucleos=cantidad_nucleos,
                config_disco=config_disco,
                software=software,
                ip_interna=ip_interna,
                ip_externa=ip_externa,
                no_serie=no_serie,
                licencia_so=licencia_so,
                tipo_respaldo=tipo_respaldo,
                id_marca=marca,
                id_tipo=tipo_servidor
            )
            # Guardar el equipo servidor en la base de datos
            equipo_servidor.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Equipos servidores cargados exitosamente", True

def carga_impresoras(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            tipo = row.get('Tipo', None)
            marca_nombre = row.get('Marca', None)
            conexion = row.get('Conexion', None)
            modelo = row.get('Modelo', None)
            imprime_color = row.get('color', None)

            # Buscar la marca en la base de datos
            marca = ImpresorasMarcas.objects.get(marca_impresora=marca_nombre)

            # Crear una instancia de Impresoras con los datos de la fila
            impresora = Impresoras(
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_dependencia=dependencia,
                tipo_impresion=tipo,
                id_marca=marca,
                conexion=conexion,
                modelo=modelo,
                imprime_color=imprime_color
            )
            # Guardar la impresora en la base de datos
            impresora.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Impresoras cargadas exitosamente", True

def carga_proyectores(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            descripcion = row.get('descripcion', None)
            modelo = row.get('Modelo', None)
            marca_nombre = row.get('Marca', None)
            tipo = row.get('Tipo', None)
            conexion_pc = row.get('Conexion_PC', None)

            # Buscar la marca en la base de datos
            marca = ProyectoresMarcas.objects.get(marca_proyector=marca_nombre)

            # Crear una instancia de Proyectores con los datos de la fila
            proyector = Proyectores(
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_dependencia=dependencia,
                descripcion=descripcion,
                modelo=modelo,
                tipo=tipo,
                marca=marca,
                conexion_pc=conexion_pc
            )
            # Guardar el proyector en la base de datos
            proyector.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Proyectores cargados exitosamente", True

def carga_drones(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            marca = row.get('Marca', None)
            modelo = row.get('Modelo', None)
            tipo_uso = row.get('tipo_uso', None)
            tipo_dron = row.get('tipo_dron', None)
            caracteristicas = row.get('caracteristicas', None)
            bateria = row.get('bateria', None)

            # Crear una instancia de Drones con los datos de la fila
            drone = Drones(
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_dependencia=dependencia,
                marca=marca,
                tipo=modelo,
                tipo_uso=tipo_uso,
                tipo_dron=tipo_dron,
                caracteristicas=caracteristicas,
                bateria=bateria
            )
            # Guardar el drone en la base de datos
            drone.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Drones cargados exitosamente", True

def carga_firewalls(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            marca = row.get('Marca', None)
            modelo = row.get('Modelo', None)
            tipo = row.get('Tipo', None)
            ram = row.get('Ram', None)
            almacenamiento = row.get('Almacenamiento', None)
            chasis = row.get('chasis', None)
            cant_fuentes_poder = row.get('fuente_poder', None)
            troughput = row.get('Troughput', None)

            # Crear una instancia de Firewalls con los datos de la fila
            firewall = Firewalls(
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_dependencia=dependencia,
                tipo=tipo,
                ram=ram,
                almacenamiento=almacenamiento,
                chasis=chasis,
                cant_fuentes_poder=cant_fuentes_poder,
                modelo=modelo,
                troughput=troughput,
                id_marca=marca
            )
            # Guardar el firewall en la base de datos
            firewall.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Firewalls cargados exitosamente", True

def carga_routers(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            marca = row.get('Marca', None)
            modelo = row.get('Modelo', None)
            no_serie = row.get('n_serie', None)
            tipo = row.get('Tipo', None)
            num_tarjetas = row.get('num_tarjeta', None)

            # Crear una instancia de Routers con los datos de la fila
            router = Routers(
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_dependencia=dependencia,
                marca=marca,
                modelo=modelo,
                no_serie=no_serie,
                tipo=tipo,
                num_tarjetas=num_tarjetas
            )
            # Guardar el router en la base de datos
            router.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Routers cargados exitosamente", True

def carga_herramientas_desarrollo(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            nombre = row.get('Nombre', None)
            version_herramienta = row.get('Version_Herramienta', None)
            uso_licencia = row.get('Uso_Licencia', None)
            uso_sin_licencia = row.get('Uso_Sin_Licencia', None)
            tipo = row.get('Tipo', None)
            descripcion = row.get('descripcion', None)

            # Crear una instancia de HerramientaDeDesarrollo con los datos de la fila
            herramienta = HerramientaDeDesarrollo(
                id_dependencia=dependencia,
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                nombre=nombre,
                version_herramienta=version_herramienta,
                uso_licencia=uso_licencia,
                uso_sin_licencia=uso_sin_licencia,
                tipo_licencias=tipo,
                descripcion=descripcion
            )
            # Guardar la herramienta en la base de datos
            herramienta.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Herramientas de desarrollo cargadas exitosamente", True

def carga_sistemas_informacion(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            nombre_sistema_info = row.get('Nombre', None)
            tipo = row.get('Tipo', None)
            esquema = row.get('Esquema', None)
            lenguaje = row.get('Lenguaje_Programacion', None)
            bd = row.get('DB', None)
            derechos = row.get('derechos', None)
            uso = row.get('Uso', None)
            supervisores = row.get('Supervisores', None)
            operacionales = row.get('Operacionales', None)
            ejecutivos = row.get('Ejecutivos', None)
            anios_en_operacion = row.get('AnioOperacion', None)

            # Crear una instancia de SistemasInformacionNombres con el nombre del sistema de información
            nombre_sistema_info_instancia, _ = SistemasInformacionNombres.objects.get_or_create(nombre_sistemainfo=nombre_sistema_info)

            # Crear una instancia de SistemasInformacion con los datos de la fila
            sistema_info = SistemasInformacion(
                id_dependencia=dependencia,
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_nombre=nombre_sistema_info_instancia,
                tipo=tipo,
                esquema=esquema,
                lenguaje=lenguaje,
                bd=bd,
                derechos=derechos,
                uso=uso,
                supervisores=supervisores,
                operacionales=operacionales,
                ejecutivos=ejecutivos,
                anios_en_operacion=anios_en_operacion
            )
            # Guardar el sistema de información en la base de datos
            sistema_info.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Sistemas de información cargados exitosamente", True

def carga_sistemas_informacion_movil(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('inventario', None)
            nombre = row.get('Nombre', None)
            descripcion = row.get('descripcion', None)
            tipo = row.get('Tipo', None)
            plataforma = row.get('Plataforma', None)
            tipo_desarrollo = row.get('Framework', None)
            bd = row.get('BD', None)
            uso = row.get('Uso', None)
            derechos = row.get('Derechos', None)
            disponible = row.get('Disponibilidad', None)
            supervisores = row.get('Supervisores', None)
            operacionales = row.get('Operacionales', None)
            ejecutivos = row.get('Ejecutivos', None)
            nombre_id = row.get('id_nombre', None)

            # Obtener o crear la instancia de SistemaInformacionMovilNombres
            sistema_nombre, _ = SistemaInformacionMovilNombres.objects.get_or_create(nombre_sistemainfo=nombre)

            # Crear una instancia de SistemaDeInformacionMovil con los datos de la fila
            sistema_informacion_movil = SistemaDeInformacionMovil(
                id_dependencia=dependencia,
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                plataforma=plataforma,
                tipo_desarrollo=tipo_desarrollo,
                framework=tipo_desarrollo,
                bd=bd,
                opc=True,  # Ajusta este valor según corresponda
                disponible=disponible,
                cantidad_supervisores=supervisores,
                anios_en_operacion=operacionales,
                descripcion=descripcion,
                tipo=tipo,
                uso=uso,
                derechos=derechos,
                supervisores=supervisores,
                operacionales=operacionales,
                ejecutivos=ejecutivos,
                id_nombre=sistema_nombre
            )
            # Guardar el sistema de información móvil en la base de datos
            sistema_informacion_movil.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Sistemas de información móvil cargados exitosamente", True

def carga_enlaces(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('no_inventario', None)
            ancho_banda = row.get('Tipo', None)  # Ajusta el nombre del campo según corresponda
            domicilio = row.get('domicilio', None)
            municipio_nombre = row.get('Municipio', None)  # Ajusta el nombre del campo según corresponda
            tipo_enlace_nombre = row.get('Tipo', None)  # Ajusta el nombre del campo según corresponda
            
            # Buscar el municipio en la base de datos o crear uno nuevo si no existe
            municipio, _ = Municipios.objects.get_or_create(municipio=municipio_nombre)
            
            # Buscar el tipo de enlace en la base de datos o crear uno nuevo si no existe
            tipo_enlace, _ = EnlacesTipos.objects.get_or_create(tipo_enlace=tipo_enlace_nombre)

            # Crear una instancia de Enlaces con los datos de la fila
            enlace = Enlaces(
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_dependencia=dependencia,
                ancho_banda=ancho_banda,
                domicilio=domicilio,
                id_municipio=municipio,
                id_tipo=tipo_enlace
            )
            # Guardar el enlace en la base de datos
            enlace.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Enlaces cargados exitosamente", True

def carga_sites(df, anio, dependencia_id):
    errores = []  # Lista para almacenar los errores encontrados
    dependencia = Dependencias.objects.get(id=dependencia_id)
    for index, row in df.iterrows():
        try:
            # Extraer los datos de cada fila del DataFrame
            no_inventario = row.get('no_inventario', None)
            metros = row.get('Site_Metros', None)
            capacidad_aire = row.get('Site_Aire_Capacidad', None)
            tipo_piso = row.get('Site_Piso', None)
            incendio = row.get('Site_Incendio', None)
            cableado = row.get('Site_Cableado', None)
            respaldo_energia = row.get('Respaldo_Energia', None)
            domicilio = row.get('domicilio', None)
            municipio_nombre = row.get('Municipio', None)  # Ajusta el nombre del campo según corresponda
            
            # Buscar el municipio en la base de datos o crear uno nuevo si no existe
            municipio, _ = Municipios.objects.get_or_create(municipio=municipio_nombre)

            # Crear una instancia de Sites con los datos de la fila
            site = Sites(
                fecha=anio,
                no_inventario=no_inventario,
                activo=True,
                id_dependencia=dependencia,
                metros=metros,
                capacidad_aire=capacidad_aire,
                tipo_piso=tipo_piso,
                incendio=incendio,
                cableado=cableado,
                respaldo_energia=respaldo_energia,
                domicilio=domicilio,
                id_municipio=municipio
            )
            # Guardar el site en la base de datos
            site.save()
        except Exception as e:
            print(e)
            errores.append(f"Línea {index + 2}: {str(e)}\n")  # Sumar 2 porque los índices de las filas comienzan desde 0 y queremos que empiece desde 1
            continue

    if errores:
        # Devolver un string con los errores encontrados
        return f"Error(es) en la(s) línea(s): {', '.join(errores)}", False
    else:
        return "Sites cargados exitosamente", True
