
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class AlmacenamientoMarcas(models.Model):
    marca_almacenamiento = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'almacenamiento_marcas'


class Almacenamientos(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey('Dependencias', models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    capacidad = models.CharField(max_length=250, blank=True, null=True)
    tipo = models.CharField(max_length=250, blank=True, null=True)
    id_marca = models.ForeignKey(AlmacenamientoMarcas, models.DO_NOTHING, db_column='id_marca', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'almacenamientos'


class Asignacion(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_tecnologia = models.ForeignKey('Tecnologias', models.DO_NOTHING, db_column='id_tecnologia', blank=True, null=True)
    id_dependencia = models.ForeignKey('Dependencias', models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignacion'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categorias(models.Model):
    nombre_categoria = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class Conmutadores(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey('Dependencias', models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    tecnologia = models.CharField(max_length=255, blank=True, null=True)
    protocolo = models.CharField(max_length=255, blank=True, null=True)
    ext_soportadas = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    id_marca = models.ForeignKey('ConmutadoresMarcas', models.DO_NOTHING, db_column='id_marca', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conmutadores'


class ConmutadoresMarcas(models.Model):
    marca_conmutador = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conmutadores_marcas'


class ConmutadoresPuertos(models.Model):
    id_conmutador = models.OneToOneField(Conmutadores, models.DO_NOTHING, db_column='id_conmutador', primary_key=True)  # The composite primary key (id_conmutador, puerto) found, that is not supported. The first column is selected.
    puerto = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'conmutadores_puertos'
        unique_together = (('id_conmutador', 'puerto'),)


class Dependencias(models.Model):
    nombre_dependencia = models.TextField(blank=True, null=True)
    id_secretaria = models.ForeignKey('Secretarias', models.DO_NOTHING, db_column='id_secretaria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dependencias'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Drones(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    tipo_uso = models.CharField(max_length=250, blank=True, null=True)
    num_rotores = models.CharField(max_length=250, blank=True, null=True)
    metodo_vuelo = models.CharField(max_length=255, blank=True, null=True)
    radio_alcance = models.CharField(max_length=250, blank=True, null=True)
    resolucion_camara = models.CharField(max_length=255, blank=True, null=True)
    bateria = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drones'


class DronesAsignacionCaracteristicas(models.Model):
    id_dron = models.OneToOneField(Drones, models.DO_NOTHING, db_column='id_dron', primary_key=True)  # The composite primary key (id_dron, id_caracteristica) found, that is not supported. The first column is selected.
    id_caracteristica = models.ForeignKey('DronesCaracteristicas', models.DO_NOTHING, db_column='id_caracteristica')

    class Meta:
        managed = False
        db_table = 'drones_asignacion_caracteristicas'
        unique_together = (('id_dron', 'id_caracteristica'),)


class DronesCaracteristicas(models.Model):
    caracteristica = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drones_caracteristicas'


class EnergiaMarcas(models.Model):
    marca_energia = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'energia_marcas'


class Energias(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    capacidad = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    id_marca = models.ForeignKey(EnergiaMarcas, models.DO_NOTHING, db_column='id_marca', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'energias'


class Enlaces(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    ancho_banda = models.CharField(max_length=100, blank=True, null=True)
    domicilio = models.TextField(blank=True, null=True)
    id_municipio = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)
    id_tipo = models.ForeignKey('EnlacesTipos', models.DO_NOTHING, db_column='id_tipo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enlaces'


class EnlacesTipos(models.Model):
    tipo_enlace = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enlaces_tipos'


class EquipoTelefonico(models.Model):
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    tipo_tel = models.CharField(max_length=255, blank=True, null=True)
    tipo_linea = models.CharField(max_length=255, blank=True, null=True)
    tipo_ext = models.CharField(max_length=255, blank=True, null=True)
    num = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipo_telefonico'


class EquiposPersonales(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    tipo = models.CharField(max_length=55, blank=True, null=True)
    modelo = models.CharField(max_length=55, blank=True, null=True)
    velocidad_procesador = models.CharField(max_length=55, blank=True, null=True)
    ram = models.CharField(max_length=30, blank=True, null=True)
    so = models.CharField(max_length=255, blank=True, null=True)
    almacenamiento = models.CharField(max_length=55, blank=True, null=True)
    cantidad_puertos = models.IntegerField(blank=True, null=True)
    capacidad_disco = models.CharField(max_length=55, blank=True, null=True)
    arquitectura = models.CharField(max_length=10, blank=True, null=True)
    licencia = models.BooleanField(blank=True, null=True)
    resolucion = models.CharField(max_length=25, blank=True, null=True)
    tipo_pantalla = models.CharField(max_length=255, blank=True, null=True)
    conexion_pantalla = models.CharField(max_length=255, blank=True, null=True)
    tamano = models.CharField(max_length=55, blank=True, null=True)
    id_marca = models.ForeignKey('EquiposPersonalesMarcas', models.DO_NOTHING, db_column='id_marca', blank=True, null=True)
    mac_alambrica = models.CharField(max_length=50, blank=True, null=True)
    mac_inalambrica = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipos_personales'


class EquiposPersonalesMarcas(models.Model):
    marca_equipopersonal = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipos_personales_marcas'


class EquiposPersonalesPuertos(models.Model):
    id_equipo_personal = models.OneToOneField(EquiposPersonales, models.DO_NOTHING, db_column='id_equipo_personal', primary_key=True)  # The composite primary key (id_equipo_personal, id_puerto) found, that is not supported. The first column is selected.
    id_puerto = models.ForeignKey('EquiposPersonalesTipopuertos', models.DO_NOTHING, db_column='id_puerto')
    mac = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipos_personales_puertos'
        unique_together = (('id_equipo_personal', 'id_puerto'),)


class EquiposPersonalesTipopuertos(models.Model):
    tipo = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipos_personales_tipopuertos'


class EquiposServidores(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    criticidad = models.CharField(max_length=255, blank=True, null=True)
    proposito = models.CharField(max_length=255, blank=True, null=True)
    velocidad = models.CharField(max_length=255, blank=True, null=True)
    ram = models.CharField(max_length=100, blank=True, null=True)
    opc = models.BooleanField(blank=True, null=True)
    almacenamiento = models.CharField(max_length=255, blank=True, null=True)
    periodo_respaldo = models.CharField(max_length=255, blank=True, null=True)
    cantidad_nucleos = models.CharField(max_length=100, blank=True, null=True)
    config_disco = models.CharField(max_length=255, blank=True, null=True)
    software = models.CharField(max_length=100, blank=True, null=True)
    ip_interna = models.CharField(max_length=100, blank=True, null=True)
    ip_externa = models.CharField(max_length=100, blank=True, null=True)
    no_serie = models.CharField(max_length=100, blank=True, null=True)
    licencia_so = models.BooleanField(blank=True, null=True)
    tipo_respaldo = models.CharField(max_length=100, blank=True, null=True)
    id_marca = models.ForeignKey('EquiposServidoresMarcas', models.DO_NOTHING, db_column='id_marca', blank=True, null=True)
    id_tipo = models.ForeignKey('EquiposServidoresTipos', models.DO_NOTHING, db_column='id_tipo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipos_servidores'


class EquiposServidoresMarcas(models.Model):
    marca_equipopersonal = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipos_servidores_marcas'


class EquiposServidoresProcesadores(models.Model):
    id_equipo_servidor = models.OneToOneField(EquiposServidores, models.DO_NOTHING, db_column='id_equipo_servidor', primary_key=True)  # The composite primary key (id_equipo_servidor, procesador) found, that is not supported. The first column is selected.
    procesador = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'equipos_servidores_procesadores'
        unique_together = (('id_equipo_servidor', 'procesador'),)


class EquiposServidoresPuertos(models.Model):
    id_equipo_servidor = models.OneToOneField(EquiposServidores, models.DO_NOTHING, db_column='id_equipo_servidor', primary_key=True)  # The composite primary key (id_equipo_servidor, puerto) found, that is not supported. The first column is selected.
    puerto = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'equipos_servidores_puertos'
        unique_together = (('id_equipo_servidor', 'puerto'),)


class EquiposServidoresTipos(models.Model):
    tipo_equipopersonal = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipos_servidores_tipos'


class Firewalls(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    cant_puertos = models.CharField(max_length=255, blank=True, null=True)
    tipo_almacenamiento = models.CharField(max_length=255, blank=True, null=True)
    almacenamiento = models.CharField(max_length=255, blank=True, null=True)
    ram = models.CharField(max_length=255, blank=True, null=True)
    chasis = models.CharField(max_length=255, blank=True, null=True)
    cant_fuentes_poder = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    troughput = models.CharField(max_length=255, blank=True, null=True)
    id_marca = models.ForeignKey('FirewallsMarcas', models.DO_NOTHING, db_column='id_marca', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'firewalls'


class FirewallsMarcas(models.Model):
    marca_firewall = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'firewalls_marcas'


class HerramientaDeDesarrollo(models.Model):
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    cantidad_licencias = models.CharField(max_length=100, blank=True, null=True)
    tipo_licencias = models.CharField(max_length=255, blank=True, null=True)
    version_herramienta = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    uso_licencia = models.CharField(max_length=255, blank=True, null=True)
    uso_sin_licencia = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'herramienta_de_desarrollo'


class Impresoras(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    imprime_color = models.BooleanField(blank=True, null=True)
    conexion = models.CharField(max_length=255, blank=True, null=True)
    tipo_impresion = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    id_marca = models.ForeignKey('ImpresorasMarcas', models.DO_NOTHING, db_column='id_marca', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impresoras'


class ImpresorasMarcas(models.Model):
    marca_impresora = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impresoras_marcas'


class Municipios(models.Model):
    municipio = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipios'


class Proyectores(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    forma_conexion_internet = models.CharField(max_length=100, blank=True, null=True)
    conexion_pc = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    marca = models.ForeignKey('ProyectoresMarcas', models.DO_NOTHING, db_column='marca', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyectores'


class ProyectoresMarcas(models.Model):
    marca_proyector = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyectores_marcas'


class Roles(models.Model):
    rol = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Routers(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    no_serie = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    num_tarjetas = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routers'


class Secretarias(models.Model):
    nombre_secretaria = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secretarias'


class SistemaDeInformacionMovil(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    plataforma = models.CharField(max_length=255, blank=True, null=True)
    tipo_desarrollo = models.CharField(max_length=255, blank=True, null=True)
    framework = models.CharField(max_length=255, blank=True, null=True)
    bd = models.CharField(max_length=255, blank=True, null=True)
    opc = models.BooleanField(blank=True, null=True)
    disponible = models.CharField(max_length=255, blank=True, null=True)
    cantidad_supervisores = models.CharField(max_length=255, blank=True, null=True)
    anios_en_operacion = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    uso = models.CharField(max_length=255, blank=True, null=True)
    derechos = models.CharField(max_length=255, blank=True, null=True)
    supervisores = models.CharField(max_length=255, blank=True, null=True)
    operacionales = models.CharField(max_length=255, blank=True, null=True)
    ejecutivos = models.CharField(max_length=255, blank=True, null=True)
    id_nombre = models.ForeignKey('SistemaInformacionMovilNombres', models.DO_NOTHING, db_column='id_nombre', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sistema_de_informacion_movil'


class SistemaInformacionMovilNombres(models.Model):
    nombre_sistemainfo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sistema_informacion_movil_nombres'


class SistemasInformacion(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    esquema = models.CharField(max_length=255, blank=True, null=True)
    lenguaje = models.CharField(max_length=255, blank=True, null=True)
    bd = models.CharField(max_length=255, blank=True, null=True)
    opc = models.BooleanField(blank=True, null=True)
    uso = models.CharField(max_length=255, blank=True, null=True)
    cantidad_supervisores = models.CharField(max_length=100, blank=True, null=True)
    anios_en_operacion = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    derechos = models.BooleanField(blank=True, null=True)
    supervisores = models.CharField(max_length=100, blank=True, null=True)
    operacionales = models.CharField(max_length=100, blank=True, null=True)
    ejecutivos = models.CharField(max_length=100, blank=True, null=True)
    id_nombre = models.ForeignKey('SistemasInformacionNombres', models.DO_NOTHING, db_column='id_nombre', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sistemas_informacion'


class SistemasInformacionNombres(models.Model):
    nombre_sistemainfo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sistemas_informacion_nombres'


class Sites(models.Model):
    fecha = models.DateField(blank=True, null=True)
    no_inventario = models.CharField(max_length=250, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    metros = models.FloatField(blank=True, null=True)
    opc = models.BooleanField(blank=True, null=True)
    capacidad_aire = models.CharField(max_length=255, blank=True, null=True)
    tipo_piso = models.CharField(max_length=255, blank=True, null=True)
    incendio = models.CharField(max_length=255, blank=True, null=True)
    cableado = models.BooleanField(blank=True, null=True)
    respaldo_energia = models.BooleanField(blank=True, null=True)
    domicilio = models.TextField(blank=True, null=True)
    id_municipio = models.ForeignKey(Municipios, models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sites'


class Tecnologias(models.Model):
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnologias'

class UsuarioManager(BaseUserManager):
    def create_user(self, email, contrasenia=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(contrasenia)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, contrasenia=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, contrasenia, **extra_fields)
class Usuarios(AbstractBaseUser, PermissionsMixin):
    id_dependencia = models.ForeignKey(Dependencias, models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    email = models.CharField(max_length=255, unique=True)
    contrasenia = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    id_rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='id_rol', blank=True, null=True)
    apellido_paterno = models.CharField(max_length=50, blank=True, null=True)
    apellio_materno = models.CharField(max_length=50, blank=True, null=True)
    num_empleado = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    #PASSWORD_FIELD = 'contrasenia'
    objects = UsuarioManager()

    def __str__(self):
        return self.email

    class Meta:
        managed = False
        db_table = 'main_usuarios'
