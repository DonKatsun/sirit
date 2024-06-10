from django import forms
from .models import *
from datetime import date
from collections import OrderedDict

class ConmutadorForm(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )

    class Meta:
        model = Conmutadores
        fields = '__all__'
        labels = {
            'id_dependencia': 'Dependencia: ',
            'id_marca': 'Marca: ',
            'no_inventario': 'Inventario:',
            'fecha': 'Fecha:',
            'activo': 'Activo:',
            'tipo': 'Tipo:',
            'tecnologia': 'Tecnología:',
            'protocolo': 'Protocólo:',
            'modelo': 'Modelo:',
            'ext_soportadas': 'Ext Soportadas:',
            'secretaria': 'Secretaría:',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_marca'].widget = forms.Select(choices=[(obj.pk, obj.marca_conmutador) for obj in ConmutadoresMarcas.objects.all()])
        # Convertir self.fields a OrderedDict
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True


class ConmutadorMarcaForm(forms.ModelForm):
    class Meta:
        model = ConmutadoresMarcas
        fields = '__all__'
        labels = {
            'marca_conmutador': 'Marca de Conmutador: ',       
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ConmutadorPuertoForm(forms.ModelForm):
    class Meta:
        model = ConmutadoresPuertos
        fields = '__all__'
        labels = {
            'id_conmutador': 'ID Conmutador: ', 
            'puerto': 'Puerto: ',      
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)       

class AlmacenamientoMarcasForm(forms.ModelForm):
    class Meta:
        model = AlmacenamientoMarcas
        fields = '__all__'
        labels = {
            'marca_almacenamiento': 'Marca de Almacenamiento: ',       
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    

       

class AlmacenamientosForm(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = Almacenamientos
        fields = '__all__'
        labels = {
            'fecha' : 'Fecha:',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'capacidad':'Capacidad:',
            'tipo': 'Tipo:',
            'id_marca': 'Marca: ',
            
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True
        self.fields['id_marca'].widget = forms.Select(choices=[(obj.pk, obj.marca_almacenamiento) for obj in AlmacenamientoMarcas.objects.all()])

        

class AsignacionForms(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = '__all__'

class DependenciasForms(forms.ModelForm):
    class Meta:
        model = Dependencias
        fields = '__all__'

class DronesForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = Drones
        fields = '__all__'
        labels = {
            'fecha' : 'Fecha:',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'marca': 'Marca: ',
            'tipo':'Tipo:',
            'tipo_uso':'Tipo de Uso:',
            'num_rotores': 'Número de Rotores:',
            'metodo_vuelo':'Método de Vuelo:',           
            'radio_alcance':'Radio de Alcance:',
            'resolucion_camara':'Resolución de Camara:',
            'bateria':'Bateria:',         
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True



class DronesCaracteristicasForms(forms.ModelForm):
    class Meta:
        model = DronesCaracteristicas
        fields = '__all__'
        labels = {
            'caracteristica': 'Caracteristica: ',
  
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class DronesAsignacionCaracteristicasForms(forms.ModelForm):
    class Meta:
        model = DronesAsignacionCaracteristicas
        fields = '__all__'
        labels = {
            'id_dron': 'ID Dron: ',
            'id_caracteristica': 'ID Caracteristicas: ',       
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_caracteristica'].widget = forms.Select(choices=[(obj.pk, obj.caracteristica) for obj in DronesCaracteristicas.objects.all()])


class EnergiasForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = Energias
        fields = '__all__'
        labels = {
            'fecha' : 'Fecha:',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'capacidad':'Capacidad:',
            'tipo': 'Tipo:',
            'modelo':'Modelo:',
            'id_marca': 'Marca: ',
            
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True
        self.fields['id_marca'].widget = forms.Select(choices=[(obj.pk, obj.marca_energia) for obj in EnergiaMarcas.objects.all()])


class EnergiaMarcasForms(forms.ModelForm):
    class Meta:
        model = EnergiaMarcas
        fields = '__all__'
        labels = {
            'marca_energia': 'Marca de Energia: ',    
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seleccionar un campo específico de los objetos relacionados
       
class EnlacesForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = Enlaces
        fields = '__all__'
        labels = {
            'fecha' : 'Fecha:',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'ancho_banda':'Ancho de Banda:',
            'domicilio': 'Domicilio:',
            'id_municipio':'Municipio:',
            'id_tipo': 'Tipos: ',
            
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True
        self.fields['id_tipo'].widget = forms.Select(choices=[(obj.pk, obj.tipo_enlace) for obj in EnlacesTipos.objects.all()])
        self.fields['domicilio'].widget = forms.TextInput()

class EnlacesTiposForms(forms.ModelForm):
    class Meta:
        model = EnlacesTipos
        fields = '__all__'
        labels = {
            'id_tipo': 'Tipos: ',       
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        


class EquipoTelefonicoForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = EquipoTelefonico
        fields = '__all__'
        labels = {
            'fecha' : 'Fecha:',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'tipo_tel': 'Tipo de Telefono: ',
            'tipo_linea':'Tipo de Linea:',
            'tipo_ext':'Tipo de Ext:',
            'num':'Número:',
                
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True


class EquiposPersonalesForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = EquiposPersonales
        fields = '__all__'
        labels = {
            'fecha' : 'Fecha:',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'marca': 'Marca: ',
            'tipo':'Tipo:',
            'modelo':'Modelo:',
            'velocidad_procesador': 'Velocidad del Procesador:',
            'ram':'Ram:',
            'so':'Sistema Operativo:',
            'almacenamiento':'Almacenamiento:',
            'cantidad_puertos':'Cantidad de Puertos:',
            'capacidad_disco':'Capacidad del Disco:',
            'arquitectura':'Arquitectura:',
            'licencia':'Licencia:',
            'resolucion':'Resolución:',
            'tipo_pantalla':'Tipo de Pantalla:',
            'conexion_pantalla':'Conexión de Pantalla:',
            'tamano':'Tamaño:',
            'id_marca':'Marca:',
            'mac_alambrica':'Marca Alambrica:',
            'mac_inalambrica':'Marca Inalambrica:',

                
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True
        self.fields['id_marca'].widget = forms.Select(choices=[(obj.pk, obj.marca_equipopersonal) for obj in EquiposPersonalesMarcas.objects.all()])


class EquiposPersonalesMarcasForms(forms.ModelForm):
    class Meta:
        model = EquiposPersonalesMarcas
        fields = '__all__'
        labels = {
            'marca_equipopersonal' : 'Marca de Equipo:',
            
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seleccionar un campo específico de los objetos relacionados
        

class EquiposPersonalesPuertosForms(forms.ModelForm):
    class Meta:
        model = EquiposPersonalesPuertos
        fields = '__all__'
        labels = {
            'id_equipo_personal' : 'ID Equipo Personal:',
            'id_puerto' : 'ID Puerto:',
            'mac' : 'MAC:',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seleccionar un campo específico de los objetos relacionados
        self.fields['id_puerto'].widget = forms.Select(choices=[(obj.pk, obj.tipo) for obj in EquiposPersonalesTipopuertos.objects.all()])

class EquiposPersonalesTipoForms(forms.ModelForm):
    class Meta:
        model = EquiposPersonalesTipopuertos
        fields = '__all__'
        labels = {
            'tipo' : 'Tipo Puerto:',

        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seleccionar un campo específico de los objetos relacionados
       
class EquiposServidoresForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = EquiposServidores
        fields = '__all__'
        labels = {
            'fecha' : 'Fecha:',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'tipo':'Tipo:',
            'criticidad':'Criticidad:',
            'proposito': 'Proposito:',
            'velocidad':'Velocidad:',
            'ram':'Ram:',
            'opc':'OPC:',
            'almacenamiento':'Almacenamiento:',
            'periodo_respaldo':'Periodo de Respaldo:',
            'cantidad_nucleos':'Cantidad de Nucleos:',
            'config_disco':'Configuración de Disco:',
            'software':'Software:',
            'ip_interna':'IP Interna:',
            'ip_externa':'IP Externa:',
            'no_serie':'Número de Serie:',
            'licencia_so':'Licencia Sistema Operativo:',
            'tipo_respaldo':'Tipo de Respaldo:',
            'id_marca':'Marca:',
            'id_tipo':'Tipos:',
       
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True
        self.fields['id_marca'].widget = forms.Select(choices=[(obj.pk, obj.marca_equipopersonal) for obj in EquiposServidoresMarcas.objects.all()])
        self.fields['id_tipo'].widget = forms.Select(choices=[(obj.pk, obj.tipo_equipopersonal) for obj in EquiposServidoresTipos.objects.all()])

    

class EquiposServidoresMarcasForms(forms.ModelForm):
    class Meta:
        model = EquiposServidoresMarcas
        fields = '__all__'
        labels = {
            'marca_equipopersonal' : 'Marca Equipo Servidor:',

        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
       

class EquiposServidoresProcesadoresForms(forms.ModelForm):
    class Meta:
        model = EquiposServidoresProcesadores
        fields = '__all__'
        labels = {
            'id_equipo_servidor' : 'ID Equipo Servidor:',
            'procesador' : 'Procesador:',
        }
        
class EquiposServidoresPuertosForms(forms.ModelForm):
    class Meta:
        model = EquiposServidoresPuertos
        fields = '__all__'
        labels = {
            'id_equipo_servidor' : 'ID Equipo Servidor:',
            'puerto' : 'Puerto:',
        }

class EquiposServidoresTiposForms(forms.ModelForm):
    class Meta:
        model = EquiposServidoresTipos
        fields = '__all__'
        labels = {
            'tipo_equipopersonal' : 'Tipo de Equipo Personal:',
            
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
      

class FirewallsForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = Firewalls
        fields = '__all__'
        labels = {
            'fecha': 'Fecha: ',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'tipo': 'Tipo:',
            'cant_puertos': 'Cantidad de Puertos:',
            'tipo_almacenamiento':'Tipo de Almacenamiento:',
            'almacenamiento':'Almacenamiento:',
            'ram': 'Ram: ',
            'chasis': 'Chasis: ',
            'cant_fuentes_poder':'Cantidad de Fuentes de Poder:',
            'modelo':'Modelo:',
            'troughput':'Troughput:',
            'id_marca': 'Marca: ',  
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True
        self.fields['id_marca'].widget = forms.Select(choices=[(obj.pk, obj.marca_firewall) for obj in FirewallsMarcas.objects.all()])

class FirewallsMarcasForms(forms.ModelForm):
    class Meta:
        model = FirewallsMarcas
        fields = '__all__'
        labels = {
            'marca_firewall' : 'Marca Firewall:',
            
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seleccionar un campo específico de los objetos relacionados
      

class HerramientaDeDesarrolloForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = HerramientaDeDesarrollo
        fields = '__all__'
        labels = {
            'fecha': 'Fecha: ',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'nombre': 'Nombre:',
            'cantidad_licencias': 'Cantidad de Licencias:',
            'tipo_licencias':'Tipo de Licencias:',
            'version_herramienta':'Versión de Herramienta:',
            'descripcion': 'Descripción: ',
            'uso_licencia': 'Uso Licencia: ',
            'uso_sin_licencia':'Uso sin Licencia:',
          
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True
        self.fields['descripcion'].widget = forms.TextInput() 

class ImpresorasForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = Impresoras
        fields = '__all__'
        labels = {
            'fecha': 'Fecha: ',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'imprime_color': 'Imprime Color:',
            'conexion': 'Conexión :',
            'tipo_impresion':'Tipo de Impresión:',
            'modelo':'Modelo:',
            'id_marca': 'Marca: ',
            
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True
        self.fields['id_marca'].widget = forms.Select(choices=[(obj.pk, obj.marca_impresora) for obj in ImpresorasMarcas.objects.all()])
      

class ImpresorasMarcasForms(forms.ModelForm):
    class Meta:
        model = ImpresorasMarcas
        fields = '__all__'
        labels = {
            'marca_impresora' : 'Marca Impresora:',
            
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seleccionar un campo específico de los objetos relacionados
      
class MunicipiosForms(forms.ModelForm):
    class Meta:
        model = Municipios
        fields = '__all__'
        labels = {
            'municipio': 'Municipio: ',       
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class ProyectoresForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = Proyectores
        fields = '__all__'
        labels = {
            'fecha': 'Fecha: ',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'forma_conexion_internet': 'Forma de Conexion a Internet:',
            'conexion_pc': 'Conexión PC:',
            'descripcion':'Descripción:',
            'modelo':'Modelo:',
            'tipo': 'Tipo: ',
            'marca': 'Marca: ',
            
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True
        self.fields['marca'].widget = forms.Select(choices=[(obj.pk, obj.marca_proyector) for obj in ProyectoresMarcas.objects.all()])
        self.fields['descripcion'].widget = forms.TextInput()  
class ProyectoresMarcasForms(forms.ModelForm):
    class Meta:
        model = ProyectoresMarcas
        fields = '__all__'
        labels = {
            'marca_proyector': 'Marca Proyector: ',       
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seleccionar un campo específico de los objetos relacionados
      

class RoutersForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = Routers
        fields = '__all__'
        labels = {
            'fecha' : 'Fecha:',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'marca': 'Marca: ',
            'modelo': 'Modelo:',
            'no_serie':'Serie:',
            'tipo':'Tipo:',
            'num_tarjetas':'Número Tarjetas:',          
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True

class RolesForms(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
        labels = {
            'rol': 'Rol: ',       
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seleccionar un campo específico de los objetos relacionados
      

class SecretariasForms(forms.ModelForm):
    class Meta:
        model = Secretarias
        fields = '__all__'
        labels = {
            'nombre_secretaria': 'Secretaría: ',       
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields['nombre_secretaria'].widget = forms.TextInput()  


class SistemaDeInformacionMovilForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = SistemaDeInformacionMovil
        fields = '__all__'
        labels = {
            'fecha': 'Fecha: ',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'plataforma': 'Plataforma:',
            'tipo_desarrollo': 'Tipo de desarrollo:',
            'framework':'Framework:',
            'bd':'BD:',
            'opc':'OPC:',
            'disponible': 'Disponible: ',
            'cantidad_supervisores': 'Cantidad de Supervisores: ',
            'anios_en_operacion': 'Años en Operación: ',
            'descripcion': 'Descripción: ',
            'tipo': 'Tipo: ',
            'uso': 'Uso: ',
            'derechos': 'Derechos: ',
            'supervisores': 'Supervisores: ',
            'operacionales': 'Operacionales: ',
            'ejecutivos': 'Ejecutivos: ',
            'id_nombre': 'Nombre: ',

            
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True
        self.fields['id_nombre'].widget = forms.Select(choices=[(obj.pk, obj.nombre_sistemainfo) for obj in SistemaInformacionMovilNombres.objects.all()])
        self.fields['descripcion'].widget = forms.TextInput()


class SistemaInformacionMovilNombresForms(forms.ModelForm):
    class Meta:
        model = SistemaInformacionMovilNombres
        fields = '__all__'
        labels = {
            'nombre_sistemainfo': 'Nombre de Sistema de Información Movíl: ',       
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
       

class SistemasInformacionForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = SistemasInformacion
        fields = '__all__'
        labels = {
            'fecha': 'Fecha: ',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'esquema': 'Esquema:',
            'lenguaje': 'Lenguaje:',
            'bd':'BD:',
            'opc':'OPC:',
            'uso': 'Uso: ',
            'cantidad_supervisores': 'Cantidad de Supervisores: ',
            'anios_en_operacion': 'Años en Operación: ',
            'descripcion': 'Descripción: ',
            'tipo': 'Tipo: ',
            'derechos': 'Derechos: ',
            'supervisores': 'Supervisores: ',
            'operacionales': 'Operacionales: ',
            'ejecutivos': 'Ejecutivos: ',
            'id_nombre': 'Nombre: ',

            
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True
        self.fields['id_nombre'].widget = forms.Select(choices=[(obj.pk, obj.nombre_sistemainfo) for obj in SistemasInformacionNombres.objects.all()])
        self.fields['descripcion'].widget = forms.TextInput()

class SistemasInformacionNombresForms(forms.ModelForm):
    class Meta:
        model = SistemasInformacionNombres
        fields = '__all__'
        labels = {
            'nombre_sistemainfo': 'Nombre de Sistema de Información: ',       
        }
         
         
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
      
class SitesForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = Sites
        fields = '__all__'
        labels = {
            'fecha': 'Fecha: ',
            'no_inventario' : 'Inventario:',
            'activo': 'Activo:',
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'metros': 'Metros:',
            'opc': 'OPC:',
            'capacidad_aire':'Capacidad de Aire:',
            'tipo_piso':'Tipo de piso:',
            'incendio': 'Incendio: ',
            'cableado': 'Cableado: ',
            'respaldo_energia': 'Respaldo de Energía: ',
            'domicilio': 'Domicilio: ',
            'id_municipio': 'Municipio: ',
            
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        

        # Verificar si es una instancia existente o una nueva
        if self.instance and self.instance.pk:
            # Es una instancia existente, mostrar la fecha guardada
            self.fields['fecha'].initial = self.instance.fecha.strftime('%Y-%m-%d')
        else:
            # Es una nueva instancia, poner la fecha actual
            self.fields['fecha'].initial = date.today().strftime('%Y-%m-%d')

        # Hacer que el campo de fecha sea solo de lectura
        self.fields['fecha'].widget.attrs['readonly'] = True
        self.fields['id_municipio'].widget = forms.Select(choices=[(obj.pk, obj.municipio) for obj in Municipios.objects.all()])
        self.fields['domicilio'].widget = forms.TextInput()

class UsuariosForms(forms.ModelForm):
    secretaria = forms.ModelChoiceField(
        queryset=Secretarias.objects.all(),
        required=False,
        label="Secretaría",
    )
    class Meta:
        model = Usuarios
        fields = '__all__'
        exclude = ['usuario']

        labels = {
            'id_dependencia': 'Dependencia: ',
'secretaria': 'Secretaría:',
            'email': 'Email:',
            'contrasenia': 'Contraseña:',
            'nombre':'Nombre:',
            'telefono':'Telefono:',
            'id_rol': 'Rol: ',
            'apellido_paterno': 'Apellido Paterno: ',
            'apellio_materno': 'Apellido Materno: ',
            'num_empleado': 'Número de Empleado: ', 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields = OrderedDict(self.fields.items())
        self.fields.move_to_end('id_dependencia', False)
        self.fields.move_to_end('secretaria', False)
        self.fields['secretaria'].widget = forms.Select(choices=[(obj.pk, obj.nombre_secretaria) for obj in Secretarias.objects.all()])
        self.fields['id_dependencia'].widget = forms.Select()
        self.fields['id_rol'].widget = forms.Select(choices=[(obj.pk, obj.rol) for obj in Roles.objects.all()])


        
  

'''class LoginForm(forms.Form):
    email = forms.CharField(label='Email')
    contrasenia = forms.CharField(label='Contraseña', widget=forms.PasswordInput)'''