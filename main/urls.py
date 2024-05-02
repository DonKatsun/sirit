from django.urls import path
from .views.conmutadores_views import (
    conmutadores_list, conmutador_detail,
    conmutador_create, conmutador_update,
    conmutador_delete, 
)
from .views.login_view import (login_view,logout_view)
from .views.Nabvar_view import(Nabvar)
from .views.catalogo_view import(catalogo)
from .views.pricipal_view import (principal)
from .views.inventarios_view import (inventario,obtener_dependencias)

from .views.catalogos_views import(
    routers_list, router_detail, router_create, router_update, router_delete,
    firewalls_list, firewall_detail, firewall_create, firewall_update, firewall_delete,
    drones_list, drone_detail, drone_create, drone_update, drone_delete,
    equipo_telefonico_list, equipo_telefonico_detail, equipo_telefonico_create, equipo_telefonico_update, equipo_telefonico_delete,
    proyectores_list, proyector_detail, proyector_create, proyector_update, proyector_delete,
    impresoras_list, impresora_detail, impresora_create, impresora_update, impresora_delete,
    energias_list, energia_detail, energia_create, energia_update, energia_delete,
    almacenamientos_list, almacenamiento_detail, almacenamiento_create, almacenamiento_update, almacenamiento_delete,
    equipos_personales_list, equipo_personal_detail, equipo_personal_create, equipo_personal_update,  equipo_personal_delete,
    equipos_servidores_list, equipo_servidor_detail, equipo_servidor_create, equipo_servidor_update, equipo_servidor_delete,
    herramientas_desarrollo_list, herramienta_desarrollo_detail, herramienta_desarrollo_create, herramienta_desarrollo_update, herramienta_desarrollo_delete,
    sistemas_informacion_list, sistema_informacion_detail, sistema_informacion_create, sistema_informacion_update, sistema_informacion_delete,
    sistemas_informacion_movil_list, sistema_informacion_movil_detail, sistema_informacion_movil_create, sistema_informacion_movil_update, sistema_informacion_movil_delete,
    enlaces_list, enlace_detail, enlace_create, enlace_update, enlace_delete,
    enlaces_tipos_list, enlace_tipo_create, enlace_tipo_update, enlace_tipo_delete,
    sites_list, site_detail, site_create, site_update, site_delete,
    municipios_list, municipio_detail, municipio__create, municipio_update, municipio_delete,
    usuarios_list, usuario_detail, usuario_create, usuario_update, usuario_delete,
    
    almacenamientos_marcas_list, almacenamiento_marca_detail, almacenamiento_marca_create, almacenamiento_marca_update, almacenamiento_marca_delete,
    conmutadores_marcas_list, conmutadores_marca_detail, conmutadores_marca_create, conmutadores_marca_update, conmutadores_marca_delete,
    conmutadores_puertos_list, conmutadores_puerto_detail, conmutadores_puerto_create, conmutadores_puerto_update, conmutadores_puerto_delete,
    drones_asignaciones_list, drone_asignacion_create, drone_asignacion_update, drone_asignacion_delete,
    drones_caracteristicas_list, drones_caracteristica_create, drones_caracteristica_update, drones_caracteristica_delete,
    energia_marcas_list, energia_marca_create, energia_marca_update, energia_marca_delete,
    equipos_personales_marcas_list, equipo_personal_marca_create, equipo_personal_marca_update, equipo_personal_marca_delete, 
    
    equipos_personales_puertos_list, equipo_personal_puerto_create, equipo_personal_puerto_update, equipo_personal_puerto_delete,
    equipos_personales_tipopuertos_list, equipo_personal_tipopuerto_create, equipo_personal_tipopuerto_update, equipo_personal_tipopuerto_delete,
    equipos_servidores_marcas_list, equipo_servidor_marca_create, equipo_servidor_marca_update, equipo_servidor_marca_delete,
    equipos_servidores_procesadores_list, equipo_servidor_procesador_create, equipo_servidor_procesador_update, equipo_servidor_procesador_delete,
    equipos_servidores_puertos_list, equipo_servidor_puerto_create, equipo_servidor_puerto_update, equipo_servidor_puerto_delete,
    equipos_servidores_tipos_list, equipo_servidor_tipo_create, equipo_servidor_tipo_update, equipo_servidor_tipo_delete,
    
    firewalls_marcas_list, firewall_marca_create, firewall_marca_update, firewall_marca_delete,
    impresoras_marcas_list, impresora_marca_create, impresora_marca_update, impresora_marca_delete,
    proyectores_marcas_list, proyector_marca_create, proyector_marca_update, proyector_marca_delete,
    roles_list, rol_create,rol_update, rol_delete,
    secretarias_list, secretaria_create, secretaria_update, secretaria_delete,
    sistemas_informacion_movil_nombres_list, sistema_informacion_movil_nombre_create, sistema_informacion_movil_nombre_update, sistema_informacion_movil_nombre_delete,
    sistemas_informacion_nombres_list, sistema_informacion_nombre_create, sistema_informacion_nombre_update, sistema_informacion_nombre_delete,
    
)
from .views.carga_view import (carga)
from .views.clonar_view import (clonar)

urlpatterns = [
    # +++++++++++++ urls paginas principaless +++++++++++++
    path('login/', login_view, name='login_view'),
    path('logout', logout_view, name='logout'),
    path('Catalogo', catalogo, name='catalogo'),
    path('Nabvar', Nabvar, name='Nabvar'),
    path('principal', principal, name='principal'),
    path('inventario', inventario, name='inventario'),
    path('obtener_dependencias/', obtener_dependencias, name='obtener_dependencias'),
    path('carga', carga, name='carga'),
    path('clonar', clonar, name='clonar'),
    
    # +++++++++++++ urls conmutadores +++++++++++++++
    path('conmutador', conmutadores_list, name='conmutadores_list'),
    path('conmutador/<int:pk>/', conmutador_detail, name='conmutador_detail'),
    path('conmutador/new/', conmutador_create, name='conmutador_create'),
    path('conmutador/<int:pk>/edit/', conmutador_update, name='conmutador_update'),
    path('conmutador/<int:pk>/delete/', conmutador_delete, name='conmutador_delete'),
    
    #  ++++++++++++ urls routers +++++++++++++++++++++++++++++
    path('router', routers_list, name='routers_list'),
    path('router/<int:pk>/', router_detail, name='routers_detail'),
    path('router/new/', router_create, name='routers_create'),
    path('router/<int:pk>/edit/', router_update, name='routers_update'),
    path('router/<int:pk>/delete/', router_delete, name='routers_delete'),
    
    # +++++++++++++ urls firewall +++++++++++++++++++++++++++++++++
    path('firewall', firewalls_list, name='firewalls_list'),
    path('firewall/<int:pk>/', firewall_detail, name='firewall_detail'),
    path('firewall/new/', firewall_create, name='firewall_create'),
    path('firewall/<int:pk>/edit/', firewall_update, name='firewall_update'),
    path('firewall/<int:pk>/delete/', firewall_delete, name='firewall_delete'),
    
    #+++++++++++++++++ urls para drone ++++++++++++++++++++++++++++++++++++
    path('drone', drones_list, name='drones_list'),
    path('drone/<int:pk>/', drone_detail, name='drone_detail'),
    path('drone/new/', drone_create, name='drone_create'),
    path('drone/<int:pk>/edit/', drone_update, name='drone_update'),
    path('drone/<int:pk>/delete/', drone_delete, name='drone_delete'),
    
    #+++++++++++++++++++ urls para equipo telefonico ++++++++++++++++++++++++
    path('equipo_telefonico', equipo_telefonico_list, name='equipo_telefonico_list'),
    path('equipo_telefonico/<int:pk>/', equipo_telefonico_detail, name='equipo_telefonico_detail'),
    path('equipo_telefonico/new/', equipo_telefonico_create, name='equipo_telefonico_create'),
    path('equipo_telefonico/<int:pk>/edit/', equipo_telefonico_update, name='equipo_telefonico_update'),
    path('equipo_telefonico/<int:pk>/delete/', equipo_telefonico_delete, name='equipo_telefonico_delete'),
    
    #++++++++++++++++++++++ urls para proyectores ++++++++++++++++++++++++++
    path('proyector', proyectores_list, name='proyectores_list'),
    path('proyector/<int:pk>/', proyector_detail, name='proyector_detail'),
    path('proyector/new/', proyector_create, name='proyector_create'),
    path('proyector/<int:pk>/edit/', proyector_update, name='proyector_update'),
    path('proyector/<int:pk>/delete/', proyector_delete, name='proyector_delete'),
    
    #++++++++++++++++++++++ urls para impresoras ++++++++++++++++++++++++++
    path('impresora', impresoras_list, name='impresoras_list'),
    path('impresora/<int:pk>/', impresora_detail, name='impresora_detail'),
    path('impresora/new/', impresora_create, name='impresora_create'),
    path('impresora/<int:pk>/edit/', impresora_update, name='impresora_update'),
    path('impresora/<int:pk>/delete/', impresora_delete, name='impresora_delete'),
    
     #++++++++++++++++++++++ urls para energias ++++++++++++++++++++++++++
    path('energia', energias_list, name='energias_list'),
    path('energia/<int:pk>/', energia_detail, name='energia_detail'),
    path('energia/new/', energia_create, name='energia_create'),
    path('energia/<int:pk>/edit/', energia_update, name='energia_update'),
    path('energia/<int:pk>/delete/', energia_delete, name='energia_delete'),
    
      #++++++++++++++++++++++ urls para almacenamientos ++++++++++++++++++++++++++
    path('almacenamiento', almacenamientos_list, name='almacenamientos_list'),
    path('almacenamiento/<int:pk>/', almacenamiento_detail, name='almacenamiento_detail'),
    path('almacenamiento/new/', almacenamiento_create, name='almacenamiento_create'),
    path('almacenamiento/<int:pk>/edit/', almacenamiento_update, name='almacenamiento_update'),
    path('almacenamiento/<int:pk>/delete/', almacenamiento_delete, name='almacenamiento_delete'),
    
    #+++++++++++++++++++++++++ urls para equipo personal +++++++++++++++++++++++++++++++
    path('equipo_personal', equipos_personales_list, name='equipos_personales_list'),
    path('equipo_personal/<int:pk>/', equipo_personal_detail, name='equipo_personal_detail'),
    path('equipo_personal/new/', equipo_personal_create, name='equipo_personal_create'),
    path('equipo_personal/<int:pk>/edit/', equipo_personal_update, name='equipo_personal_update'),
    path('equipo_personal/0<int:pk>/delete/', equipo_personal_delete, name='equipo_personal_delete'),
    
    #+++++++++++++++++++++++++ urls para equipo servidor +++++++++++++++++++++++++++++++
    path('equipo_servidor', equipos_servidores_list, name='equipos_servidores_list'),
    path('equipo_servidor/<int:pk>/', equipo_servidor_detail, name='equipo_servidor_detail'),
    path('equipo_servidor/new/', equipo_servidor_create, name='equipo_servidor_create'),
    path('equipo_servidor/<int:pk>/edit/', equipo_servidor_update, name='equipo_servidor_update'),
    path('equipo_servidor/0<int:pk>/delete/', equipo_servidor_delete, name='equipo_servidor_delete'),
    
    #+++++++++++++++++++++++++ urls para herramientas de desarrollo +++++++++++++++++++++++++++++++
    path('herramienta_de_desarrollo', herramientas_desarrollo_list, name='herramientas_desarrollo_list'),
    path('herramienta_de_desarrollo/<int:pk>/', herramienta_desarrollo_detail, name='herramienta_desarrollo_detail'),
    path('herramienta_de_desarrollo/new/', herramienta_desarrollo_create, name='herramienta_desarrollo_create'),
    path('herramienta_de_desarrollo/<int:pk>/edit/', herramienta_desarrollo_update, name='herramienta_desarrollo_update'),
    path('herramienta_de_desarrollo/0<int:pk>/delete/', herramienta_desarrollo_delete, name='herramienta_desarrollo_delete'),
    
    #+++++++++++++++++++++++++ urls para sistemas de información +++++++++++++++++++++++++++++++
    path('sistema_informacion', sistemas_informacion_list, name='sistemas_informacion_list'),
    path('sistema_informacion/<int:pk>/', sistema_informacion_detail, name='sistema_informacion_detail'),
    path('sistema_informacion/new/', sistema_informacion_create, name='sistema_informacion_create'),
    path('sistema_informacion/<int:pk>/edit/', sistema_informacion_update, name='sistema_informacion_update'),
    path('sistema_informacion/0<int:pk>/delete/', sistema_informacion_delete, name='sistema_informacion_delete'),
    
    #+++++++++++++++++++++++++ urls para sistemas de información movil  +++++++++++++++++++++++++++++++
    path('sistema_informacion_movil', sistemas_informacion_movil_list, name='sistemas_informacion_movil_list'),
    path('sistema_informacion_movil/<int:pk>/', sistema_informacion_movil_detail, name='sistema_informacion_movil_detail'),
    path('sistema_informacion_movil/new/', sistema_informacion_movil_create, name='sistema_informacion_movil_create'),
    path('sistema_informacion_movil/<int:pk>/edit/', sistema_informacion_movil_update, name='sistema_informacion_movil_update'),
    path('sistema_informacion_movil/0<int:pk>/delete/', sistema_informacion_movil_delete, name='sistema_informacion_movil_delete'),
    
    #+++++++++++++++++++++++++ urls para enlace   +++++++++++++++++++++++++++++++
    path('enlace', enlaces_list, name='enlaces_list'),
    path('enlace/<int:pk>/', enlace_detail, name='enlace_detail'),
    path('enlace/new/', enlace_create, name='enlace_create'),
    path('enlace/<int:pk>/edit/', enlace_update, name='enlace_update'),
    path('enlace/0<int:pk>/delete/', enlace_delete, name='enlace_delete'),
    
    #+++++++++++++++++++++++++ urls para enlaces tipos    +++++++++++++++++++++++++++++++
    path('enlace_tipo', enlaces_tipos_list, name='enlaces_tipos_list'),
    path('enlace_tipo/new/', enlace_tipo_create, name='enlace_tipo_create'),
    path('enlace_tipo/<int:pk>/edit/', enlace_tipo_update, name='enlace_tipo_update'),
    path('enlace_tipo/0<int:pk>/delete/', enlace_tipo_delete, name='enlace_tipo_delete'),
    
     #+++++++++++++++++++++++++ urls para sites   +++++++++++++++++++++++++++++++
    path('site', sites_list, name='sites_list'),
    path('site/<int:pk>/', site_detail, name='site_detail'),
    path('site/new/', site_create, name='site_create'),
    path('site/<int:pk>/edit/', site_update, name='site_update'),
    path('site/0<int:pk>/delete/', site_delete, name='site_delete'),
    
    #+++++++++++++++++++++++++ urls para municipios   +++++++++++++++++++++++++++++++
    path('municipio', municipios_list, name='municipios_list'),
    path('municipio/<int:pk>/', municipio_detail, name='municipio_detail'),
    path('municipio/new/', municipio__create, name='municipio__create'),
    path('municipio/<int:pk>/edit/', municipio_update, name='municipio_update'),
    path('municipio/0<int:pk>/delete/', municipio_delete, name='municipio_delete'),
    
    #+++++++++++++++++++++++++ urls para usuarios   +++++++++++++++++++++++++++++++
    path('usuario', usuarios_list, name='usuarios_list'),
    path('usuario/<int:pk>/', usuario_detail, name='usuario_detail'),
    path('usuario/new/', usuario_create, name='usuario_create'),
    path('usuario/<int:pk>/edit/', usuario_update, name='usuario_update'),
    path('usuario/0<int:pk>/delete/', usuario_delete, name='usuario_delete'),
    
    #+++++++++++++++++++++++++ urls para almacenamientos marcas   +++++++++++++++++++++++++++++++
    path('almacenamiento_marca', almacenamientos_marcas_list, name='almacenamientos_marcas_list'),
    path('almacenamiento_marca/<int:pk>/', almacenamiento_marca_detail, name='almacenamiento_marca_detail'),
    path('almacenamiento_marca/new/', almacenamiento_marca_create, name='almacenamiento_marca_create'),
    path('almacenamiento_marca/<int:pk>/edit/', almacenamiento_marca_update, name='almacenamiento_marca_update'),
    path('almacenamiento_marca/0<int:pk>/delete/', almacenamiento_marca_delete, name='almacenamiento_marca_delete'),
    
   #+++++++++++++++++++++++++ urls para conmutadores marcas   +++++++++++++++++++++++++++++++
    path('conmutador_marca', conmutadores_marcas_list, name='conmutadores_marcas_list'),
    path('conmutador_marca/<int:pk>/', conmutadores_marca_detail, name='conmutadores_marca_detail'),
    path('conmutador_marca/new/', conmutadores_marca_create, name='conmutadores_marca_create'),
    path('conmutador_marca/<int:pk>/edit/', conmutadores_marca_update, name='conmutadores_marca_update'),
    path('conmutador_marca/0<int:pk>/delete/', conmutadores_marca_delete, name='conmutadores_marca_delete'),
    
    #+++++++++++++++++++++++++ urls para conmutadores puertos   +++++++++++++++++++++++++++++++
    path('conmutador_puerto', conmutadores_puertos_list, name='conmutadores_puertos_list'),
    path('conmutador_puerto/<int:pk>/', conmutadores_puerto_detail, name='conmutadores_puerto_detail'),
    path('conmutador_puerto/new/', conmutadores_puerto_create, name='conmutadores_puerto_create'),
    path('conmutador_puerto/<int:pk>/edit/', conmutadores_puerto_update, name='conmutadores_puerto_update'),
    path('conmutador_puerto/0<int:pk>/delete/', conmutadores_puerto_delete, name='conmutadores_puerto_delete'),
    
    #+++++++++++++++++++++++++ urls para asignacion caracteristicas drone   +++++++++++++++++++++++++++++++
    path('drone_asignacion', drones_asignaciones_list, name='drones_asignaciones_list'),
    path('drone_asignacion/new/', drone_asignacion_create, name='drone_asignacion_create'),
    path('drone_asignacion/<int:pk>/edit/', drone_asignacion_update, name='drone_asignacion_update'),
    path('drone_asignacion/0<int:pk>/delete/', drone_asignacion_delete, name='drone_asignacion_delete'),
    
    #+++++++++++++++++++++++++ urls para caracteristicas drone   +++++++++++++++++++++++++++++++
    path('drone_caracteristica', drones_caracteristicas_list, name='drones_caracteristicas_list'),
    path('drone_caracteristica/new/', drones_caracteristica_create, name='drones_caracteristica_create'),
    path('drone_caracteristica/<int:pk>/edit/', drones_caracteristica_update, name='drones_caracteristica_update'),
    path('drone_caracteristica/0<int:pk>/delete/', drones_caracteristica_delete, name='drones_caracteristica_delete'),
    
    #+++++++++++++++++++++++++ urls para marcas energia  +++++++++++++++++++++++++++++++
    path('energia_marca', energia_marcas_list, name='energia_marcas_list'),
    path('energia_marca/new/', energia_marca_create, name='energia_marca_create'),
    path('energia_marca/<int:pk>/edit/', energia_marca_update, name='energia_marca_update'),
    path('energia_marca/0<int:pk>/delete/', energia_marca_delete, name='energia_marca_delete'),
    
    #+++++++++++++++++++++++++ urls para equipos marca personales  +++++++++++++++++++++++++++++++
    path('equipo_personal_marca', equipos_personales_marcas_list, name='equipos_personales_marcas_list'),
    path('equipo_personal_marca/new/', equipo_personal_marca_create, name='equipo_personal_marca_create'),
    path('equipo_personal_marca/<int:pk>/edit/', equipo_personal_marca_update, name='equipo_personal_marca_update'),
    path('equipo_personal_marca/0<int:pk>/delete/', equipo_personal_marca_delete, name='equipo_personal_marca_delete'),
    
    #+++++++++++++++++++++++++ urls para equipos puertos personales  +++++++++++++++++++++++++++++++
    path('equipo_personal_puerto', equipos_personales_puertos_list, name='equipos_personales_puertos_list'),
    path('equipo_personal_puerto/new/', equipo_personal_puerto_create, name='equipo_personal_puerto_create'),
    path('equipo_personal_puerto/<int:pk>/edit/', equipo_personal_puerto_update, name='equipo_personal_puerto_update'),
    path('equipo_personal_puerto/0<int:pk>/delete/', equipo_personal_puerto_delete, name='equipo_personal_puerto_delete'),
    
    #+++++++++++++++++++++++++ urls para equipos tipopuertos personales  +++++++++++++++++++++++++++++++
    path('equipo_personal_tipopuerto', equipos_personales_tipopuertos_list, name='equipos_personales_tipopuertos_list'),
    path('equipo_personal_tipopuerto/new/', equipo_personal_tipopuerto_create, name='equipo_personal_tipopuerto_create'),
    path('equipo_personal_tipopuerto/<int:pk>/edit/', equipo_personal_tipopuerto_update, name='equipo_personal_tipopuerto_update'),
    path('equipo_personal_tipopuerto/0<int:pk>/delete/', equipo_personal_tipopuerto_delete, name='equipo_personal_tipopuerto_delete'),
    
    #+++++++++++++++++++++++++ urls para marcas equipos servidores   +++++++++++++++++++++++++++++++
    path('equipo_servidor_marca', equipos_servidores_marcas_list, name='equipos_servidores_marcas_list'),
    path('equipo_servidor_marca/new/', equipo_servidor_marca_create, name='equipo_servidor_marca_create'),
    path('equipo_servidor_marca/<int:pk>/edit/', equipo_servidor_marca_update, name='equipo_servidor_marca_update'),
    path('equipo_servidor_marca/0<int:pk>/delete/', equipo_servidor_marca_delete, name='equipo_servidor_marca_delete'),
    
    #+++++++++++++++++++++++++ urls para procesadores equipos servidores   +++++++++++++++++++++++++++++++
    path('equipo_servidor_procesador', equipos_servidores_procesadores_list, name='equipos_servidores_procesadores_list'),
    path('equipo_servidor_procesador/new/', equipo_servidor_procesador_create, name='equipo_servidor_procesador_create'),
    path('equipo_servidor_procesador/<int:pk>/edit/', equipo_servidor_procesador_update, name='equipo_servidor_procesador_update'),
    path('equipo_servidor_procesador/0<int:pk>/delete/', equipo_servidor_procesador_delete, name='equipo_servidor_procesador_delete'),
    
    #+++++++++++++++++++++++++ urls para puertos equipos servidores   +++++++++++++++++++++++++++++++
    path('equipo_servidor_puerto', equipos_servidores_puertos_list, name='equipos_servidores_puertos_list'),
    path('equipo_servidor_puerto/new/', equipo_servidor_puerto_create, name='equipo_servidor_puerto_create'),
    path('equipo_servidor_puerto/<int:pk>/edit/', equipo_servidor_puerto_update, name='equipo_servidor_puerto_update'),
    path('equipo_servidor_puerto/0<int:pk>/delete/', equipo_servidor_puerto_delete, name='equipo_servidor_puerto_delete'),
    
    #+++++++++++++++++++++++++ urls para tipos equipos servidores   +++++++++++++++++++++++++++++++
    path('equipo_servidor_tipo', equipos_servidores_tipos_list, name='equipos_servidores_tipos_list'),
    path('equipo_servidor_tipo/new/', equipo_servidor_tipo_create, name=' equipo_servidor_tipo_create'),
    path('equipo_servidor_tipo/<int:pk>/edit/', equipo_servidor_tipo_update, name='equipo_servidor_tipo_update'),
    path('equipo_servidor_tipo/0<int:pk>/delete/', equipo_servidor_tipo_delete, name='equipo_servidor_tipo_delete'),
    
    #+++++++++++++++++++++++++ urls para Marcas Fierewalls   +++++++++++++++++++++++++++++++
    path('firewall_marca', firewalls_marcas_list, name='firewalls_marcas_list'),
    path('firewall_marca/new/', firewall_marca_create, name='firewall_marca_create'),
    path('firewall_marca/<int:pk>/edit/', firewall_marca_update, name='firewall_marca_update'),
    path('firewall_marca/0<int:pk>/delete/', firewall_marca_delete, name='firewall_marca_delete'),
    
    #+++++++++++++++++++++++++ urls para Marcas Impresoras   +++++++++++++++++++++++++++++++
    path('impresora_marca', impresoras_marcas_list, name='impresoras_marcas_list'),
    path('impresora_marca/new/', impresora_marca_create, name='impresora_marca_create'),
    path('impresora_marca/<int:pk>/edit/', impresora_marca_update, name='impresora_marca_update'),
    path('impresora_marca/0<int:pk>/delete/', impresora_marca_delete, name='impresora_marca_delete'),
    
    #+++++++++++++++++++++++++ urls para Marcas Proyectores   +++++++++++++++++++++++++++++++
    path('proyector_marca', proyectores_marcas_list, name='proyectores_marcas_list'),
    path('proyector_marca/new/', proyector_marca_create, name='proyector_marca_create'),
    path('proyector_marca/<int:pk>/edit/', proyector_marca_update, name='proyector_marca_update'),
    path('proyector_marca/0<int:pk>/delete/', proyector_marca_delete, name='proyector_marca_delete'),
    
    #+++++++++++++++++++++++++ urls para roles   +++++++++++++++++++++++++++++++
    path('rol', roles_list, name='roles_list'),
    path('rol/new/', rol_create, name='rol_create'),
    path('rol/<int:pk>/edit/', rol_update, name='rol_update'),
    path('rol/0<int:pk>/delete/', rol_delete, name='rol_delete'),
    
    #+++++++++++++++++++++++++ urls para secretarias  +++++++++++++++++++++++++++++++
    path('secretaria', secretarias_list, name='secretarias_list'),
    path('secretaria/new/', secretaria_create, name='secretaria_create'),
    path('secretaria/<int:pk>/edit/', secretaria_update, name='secretaria_update'),
    path('secretaria/0<int:pk>/delete/', secretaria_delete, name='secretaria_delete'),
    
    #+++++++++++++++++++++++++ urls para Nombres sistema de indformacaion movil   +++++++++++++++++++++++++++++++
    path('sistema_informacion_movil_nombres', sistemas_informacion_movil_nombres_list, name='sistemas_informacion_movil_nombres_list'),
    path('sistema_informacion_movil_nombres/new/', sistema_informacion_movil_nombre_create, name='sistema_informacion_movil_nombre_create'),
    path('sistema_informacion_movil_nombres/<int:pk>/edit/', sistema_informacion_movil_nombre_update, name='sistema_informacion_movil_nombre_update'),
    path('sistema_informacion_movil_nombres/0<int:pk>/delete/', sistema_informacion_movil_nombre_delete, name='sistema_informacion_movil_nombre_delete'),
    
    #+++++++++++++++++++++++++ urls para Nombres sistema de indformacaion    +++++++++++++++++++++++++++++++
    path('sistema_informacion_nombre', sistemas_informacion_nombres_list, name='sistemas_informacion_nombres_list'),
    path('sistema_informacion_nombre/new/', sistema_informacion_nombre_create, name='sistema_informacion_nombre_create'),
    path('sistema_informacion_nombre/<int:pk>/edit/', sistema_informacion_nombre_update, name='sistema_informacion_nombre_update'),
    path('sistema_informacion_nombre/0<int:pk>/delete/', sistema_informacion_nombre_delete, name='sistema_informacion_nombre_delete'),

]





















