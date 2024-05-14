from django.shortcuts import render
from django.db.models import Count, Case, When, Subquery, OuterRef, Q,Prefetch
from ..models import *
from django.contrib.auth.decorators import login_required

@login_required
def principal(request):
    selected_secretaria = request.GET.get('secretaria')
    selected_dependencia = request.GET.get('dependencia')
    selected_year = request.GET.get('year')

    secretarias = Secretarias.objects.all()
    datos_por_secretaria = None

    if selected_secretaria:
        if selected_year:
            datos_por_secretaria = Dependencias.objects.filter(id_secretaria=selected_secretaria).annotate(
                num_conmutadores=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        conmutadores__fecha__year=selected_year,
                        conmutadores__isnull=False
                    ).values('id').annotate(count=Count('conmutadores')).values('count')[:1]
                ),
                num_energias=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        energias__fecha__year=selected_year,
                        energias__isnull=False
                    ).values('id').annotate(count=Count('energias')).values('count')[:1]
                ),
                num_equipos_personales=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        equipospersonales__fecha__year=selected_year,
                        equipospersonales__isnull=False
                    ).values('id').annotate(count=Count('equipospersonales')).values('count')[:1]
                ),
                num_equipos_servidores=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        equiposservidores__fecha__year=selected_year,
                        equiposservidores__isnull=False
                    ).values('id').annotate(count=Count('equiposservidores')).values('count')[:1]
                ),
                num_impresoras=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        impresoras__fecha__year=selected_year,
                        impresoras__isnull=False
                    ).values('id').annotate(count=Count('impresoras')).values('count')[:1]
                ),
                num_proyectores=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        proyectores__fecha__year=selected_year,
                        proyectores__isnull=False
                    ).values('id').annotate(count=Count('proyectores')).values('count')[:1]
                ),
                num_enlaces=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        enlaces__fecha__year=selected_year,
                        enlaces__isnull=False
                    ).values('id').annotate(count=Count('enlaces')).values('count')[:1]
                ),
                num_drones=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        drones__fecha__year=selected_year,
                        drones__isnull=False
                    ).values('id').annotate(count=Count('drones')).values('count')[:1]
                ),
                num_firewalls=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        firewalls__fecha__year=selected_year,
                        firewalls__isnull=False
                    ).values('id').annotate(count=Count('firewalls')).values('count')[:1]
                ),
                num_routers=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        routers__fecha__year=selected_year,
                        routers__isnull=False
                    ).values('id').annotate(count=Count('routers')).values('count')[:1]
                ),
            )
        
        else:
            #print(Dependencias.objects.filter(id_secretaria=selected_secretaria))
            datos_por_secretaria = Dependencias.objects.filter(id_secretaria=selected_secretaria).annotate(
            num_conmutadores=Subquery(
                Dependencias.objects.filter(
                    id=OuterRef('id'),
                    conmutadores__isnull=False
                ).values('id').annotate(count=Count('conmutadores')).values('count')[:1]
            ),
            num_energias=Subquery(
                Dependencias.objects.filter(
                    id=OuterRef('id'),
                    energias__isnull=False
                ).values('id').annotate(count=Count('energias')).values('count')[:1]
            ),
            num_equipos_personales=Subquery(
                Dependencias.objects.filter(
                    id=OuterRef('id'),
                    equipospersonales__isnull=False
                ).values('id').annotate(count=Count('equipospersonales')).values('count')[:1]
            ),
            num_equipos_servidores=Subquery(
                Dependencias.objects.filter(
                    id=OuterRef('id'),
                    equiposservidores__isnull=False
                ).values('id').annotate(count=Count('equiposservidores')).values('count')[:1]
            ),
            num_impresoras=Subquery(
                Dependencias.objects.filter(
                    id=OuterRef('id'),
                    impresoras__isnull=False
                ).values('id').annotate(count=Count('impresoras')).values('count')[:1]
            ),
            num_proyectores=Subquery(
                Dependencias.objects.filter(
                    id=OuterRef('id'),
                    proyectores__isnull=False
                ).values('id').annotate(count=Count('proyectores')).values('count')[:1]
            ),
            num_enlaces=Subquery(
                Dependencias.objects.filter(
                    id=OuterRef('id'),
                    enlaces__isnull=False
                ).values('id').annotate(count=Count('enlaces')).values('count')[:1]
            ),
            num_drones=Subquery(
                Dependencias.objects.filter(
                    id=OuterRef('id'),
                    drones__isnull=False
                ).values('id').annotate(count=Count('drones')).values('count')[:1]
            ),
            num_firewalls=Subquery(
                Dependencias.objects.filter(
                    id=OuterRef('id'),
                    firewalls__isnull=False
                ).values('id').annotate(count=Count('firewalls')).values('count')[:1]
            ),
            num_routers=Subquery(
                Dependencias.objects.filter(
                    id=OuterRef('id'),
                    routers__isnull=False
                ).values('id').annotate(count=Count('routers')).values('count')[:1]
            ),
        )
    elif selected_year:
            datos_por_secretaria = Secretarias.objects.annotate(
                num_conmutadores=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        conmutadores__fecha__year=selected_year,
                        conmutadores__isnull=False
                    ).values('id').annotate(count=Count('conmutadores')).values('count')[:1]
                ),
                num_energias=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        energias__fecha__year=selected_year,
                        energias__isnull=False
                    ).values('id').annotate(count=Count('energias')).values('count')[:1]
                ),
                num_equipos_personales=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        equipospersonales__fecha__year=selected_year,
                        equipospersonales__isnull=False
                    ).values('id').annotate(count=Count('equipospersonales')).values('count')[:1]
                ),
                num_equipos_servidores=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        equiposservidores__fecha__year=selected_year,
                        equiposservidores__isnull=False
                    ).values('id').annotate(count=Count('equiposservidores')).values('count')[:1]
                ),
                num_impresoras=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        impresoras__fecha__year=selected_year,
                        impresoras__isnull=False
                    ).values('id').annotate(count=Count('impresoras')).values('count')[:1]
                ),
                num_proyectores=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        proyectores__fecha__year=selected_year,
                        proyectores__isnull=False
                    ).values('id').annotate(count=Count('proyectores')).values('count')[:1]
                ),
                num_enlaces=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        enlaces__fecha__year=selected_year,
                        enlaces__isnull=False
                    ).values('id').annotate(count=Count('enlaces')).values('count')[:1]
                ),
                num_drones=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        drones__fecha__year=selected_year,
                        drones__isnull=False
                    ).values('id').annotate(count=Count('drones')).values('count')[:1]
                ),
                num_firewalls=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        firewalls__fecha__year=selected_year,
                        firewalls__isnull=False
                    ).values('id').annotate(count=Count('firewalls')).values('count')[:1]
                ),
                num_routers=Subquery(
                    Dependencias.objects.filter(
                        id=OuterRef('id'),
                        routers__fecha__year=selected_year,
                        routers__isnull=False
                    ).values('id').annotate(count=Count('routers')).values('count')[:1]
                ),
            )
    else:
        datos_por_secretaria = []  # Inicializa datos_por_secretaria como una lista vacía
        datos = Secretarias.objects.values('nombre_secretaria').annotate(
        num_conmutadores=Count('dependencias__conmutadores', distinct=True),
    )
        for dato in datos:
            datos_por_secretaria.append({
                'nombre_secretaria': dato['nombre_secretaria'],
                'num_conmutadores': dato['num_conmutadores'],
            })

        datos_energias = Secretarias.objects.values('nombre_secretaria').annotate(num_energias=Count('dependencias__energias', distinct=True),)
        for i, dato in enumerate(datos_energias):   datos_por_secretaria[i]['num_energias'] = dato['num_energias']
        datos_equipos_personales = Secretarias.objects.values('nombre_secretaria').annotate(num_equipos_personales=Count('dependencias__equipospersonales', distinct=True),)
        for i, dato in enumerate(datos_equipos_personales):   datos_por_secretaria[i]['num_equipos_personales'] = dato['num_equipos_personales']
        datos_equipos_servidores = Secretarias.objects.values('nombre_secretaria').annotate(num_equipos_servidores=Count('dependencias__equiposservidores', distinct=True),)
        for i, dato in enumerate(datos_equipos_servidores):   datos_por_secretaria[i]['num_equipos_servidores'] = dato['num_equipos_servidores']
        datos_impresoras = Secretarias.objects.values('nombre_secretaria').annotate(num_impresoras=Count('dependencias__impresoras', distinct=True),)
        for i, dato in enumerate(datos_impresoras):   datos_por_secretaria[i]['num_impresoras'] = dato['num_impresoras']
        datos_proyectores = Secretarias.objects.values('nombre_secretaria').annotate(num_proyectores=Count('dependencias__proyectores', distinct=True),)
        for i, dato in enumerate(datos_proyectores):   datos_por_secretaria[i]['num_proyectores'] = dato['num_proyectores']
        datos_enlaces = Secretarias.objects.values('nombre_secretaria').annotate(num_enlaces=Count('dependencias__enlaces', distinct=True),)
        for i, dato in enumerate(datos_enlaces):   datos_por_secretaria[i]['num_enlaces'] = dato['num_enlaces']
        datos_drones = Secretarias.objects.values('nombre_secretaria').annotate(num_drones=Count('dependencias__drones', distinct=True),)
        for i, dato in enumerate(datos_drones):   datos_por_secretaria[i]['num_drones'] = dato['num_drones']
        datos_firewalls = Secretarias.objects.values('nombre_secretaria').annotate(num_firewalls=Count('dependencias__firewalls', distinct=True),)
        for i, dato in enumerate(datos_firewalls):   datos_por_secretaria[i]['num_firewalls'] = dato['num_firewalls']
        datos_routers = Secretarias.objects.values('nombre_secretaria').annotate(num_routers=Count('dependencias__routers', distinct=True),)
        for i, dato in enumerate(datos_routers):   datos_por_secretaria[i]['num_routers'] = dato['num_routers']
    #print(datos_por_secretaria)             
    return render(request, 'principal.html', {
        'secretarias': secretarias,
        'datos_por_secretaria': datos_por_secretaria,
        'selected_secretaria': selected_secretaria,
        'selected_dependencia': selected_dependencia
    })
