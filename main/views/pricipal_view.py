from django.shortcuts import render
from django.db.models import Count, Case, When, Subquery, OuterRef
from ..models import Secretarias, Dependencias

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
        datos_por_secretaria = Secretarias.objects.annotate(
            num_conmutadores=Subquery(
                Dependencias.objects.filter(
                    id_secretaria=OuterRef('id')
                ).annotate(
                    num=Count(Case(When(conmutadores__isnull=False, then=1)))
                ).values('num')[:1]
            ),
            num_energias=Subquery(
                Dependencias.objects.filter(
                    id_secretaria=OuterRef('id')
                ).annotate(
                    num=Count(Case(When(energias__isnull=False, then=1)))
                ).values('num')[:1]
            ),
            num_equipos_personales=Subquery(
                Dependencias.objects.filter(
                    id_secretaria=OuterRef('id')
                ).annotate(
                    num=Count(Case(When(equipospersonales__isnull=False, then=1)))
                ).values('num')[:1]
            ),
            num_equipos_servidores=Subquery(
                Dependencias.objects.filter(
                    id_secretaria=OuterRef('id')
                ).annotate(
                    num=Count(Case(When(equiposservidores__isnull=False, then=1)))
                ).values('num')[:1]
            ),
            num_impresoras=Subquery(
                Dependencias.objects.filter(
                    id_secretaria=OuterRef('id')
                ).annotate(
                    num=Count(Case(When(impresoras__isnull=False, then=1)))
                ).values('num')[:1]
            ),
            num_proyectores=Subquery(
                Dependencias.objects.filter(
                    id_secretaria=OuterRef('id')
                ).annotate(
                    num=Count(Case(When(proyectores__isnull=False, then=1)))
                ).values('num')[:1]
            ),
            num_enlaces=Subquery(
                Dependencias.objects.filter(
                    id_secretaria=OuterRef('id')
                ).annotate(
                    num=Count(Case(When(enlaces__isnull=False, then=1)))
                ).values('num')[:1]
            ),
            num_drones=Subquery(
                Dependencias.objects.filter(
                    id_secretaria=OuterRef('id')
                ).annotate(
                    num=Count(Case(When(drones__isnull=False, then=1)))
                ).values('num')[:1]
            ),
            num_firewalls=Subquery(
                Dependencias.objects.filter(
                    id_secretaria=OuterRef('id')
                ).annotate(
                    num=Count(Case(When(firewalls__isnull=False, then=1)))
                ).values('num')[:1]
            ),
            num_routers=Subquery(
                Dependencias.objects.filter(
                    id_secretaria=OuterRef('id')
                ).annotate(
                    num=Count(Case(When(routers__isnull=False, then=1)))
                ).values('num')[:1]
            ),
        )
    return render(request, 'principal.html', {
        'secretarias': secretarias,
        'datos_por_secretaria': datos_por_secretaria,
        'selected_secretaria': selected_secretaria,
        'selected_dependencia': selected_dependencia
    })
