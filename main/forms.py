from django import forms
from .models import *

class ConmutadorForm(forms.ModelForm):
    class Meta:
        model = Conmutadores
        fields = '__all__'
        labels = {
            'id_dependencia': 'Dependencia: ',
            'id_marca': 'Marca: ',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el widget para mostrar una opción diferente al usuario pero enviar el valor correcto
        self.fields['id_dependencia'].widget = forms.Select(choices=[(obj.pk, obj.nombre_dependencia) for obj in Dependencias.objects.all()])
        self.fields['id_marca'].widget = forms.Select(choices=[(obj.pk, obj.marca_conmutador) for obj in ConmutadoresMarcas.objects.all()])

class ConmutadorMarcaForm(forms.ModelForm):
    class Meta:
        model = ConmutadoresMarcas
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seleccionar un campo específico de los objetos relacionados
        self.fields['Dependencia'].queryset = Dependencias.objects.values_list('nombre_dependencia', flat=True)
        self.fields['id_marca'].queryset = ConmutadoresMarcas.objects.values_list('marca_conmutador', flat=True)

class AlmacenamientoMarcasForm(forms.ModelForm):
    class Meta:
        model = AlmacenamientoMarcas
        fields = '__all__'

class AlmacenamientosForm(forms.ModelForm):
    class Meta:
        model = Almacenamientos
        fields = '__all__'

class AsignacionForms(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = '__all__'

class DependenciasForms(forms.ModelForm):
    class Meta:
        model = Dependencias
        fields = '__all__'

class DronesForms(forms.ModelForm):
    class Meta:
        model = Drones
        fields = '__all__'

class DronesCaracteristicasForms(forms.ModelForm):
    class Meta:
        model = DronesCaracteristicas
        fields = '__all__'

class EnergiasForms(forms.ModelForm):
    class Meta:
        model = Energias
        fields = '__all__'

class EnergiaMarcasForms(forms.ModelForm):
    class Meta:
        model = EnergiaMarcas
        fields = '__all__'

class EnlacesForms(forms.ModelForm):
    class Meta:
        model = Enlaces
        fields = '__all__'

class EnlacesTiposForms(forms.ModelForm):
    class Meta:
        model = EnlacesTipos
        fields = '__all__'

class EquipoTelefonicoForms(forms.ModelForm):
    class Meta:
        model = EquipoTelefonico
        fields = '__all__'

class EquiposPersonalesForms(forms.ModelForm):
    class Meta:
        model = EquiposPersonales
        fields = '__all__'

class EquiposPersonalesMarcasForms(forms.ModelForm):
    class Meta:
        model = EquiposPersonalesMarcas
        fields = '__all__'

class EquiposServidoresForms(forms.ModelForm):
    class Meta:
        model = EquiposServidores
        fields = '__all__'

class EquiposServidoresMarcasForms(forms.ModelForm):
    class Meta:
        model = EquiposServidoresMarcas
        fields = '__all__'

class EquiposServidoresProcesadoresForms(forms.ModelForm):
    class Meta:
        model = EquiposServidoresProcesadores
        fields = '__all__'

class EquiposServidoresTiposForms(forms.ModelForm):
    class Meta:
        model = EquiposServidoresTipos
        fields = '__all__'

class FirewallsForms(forms.ModelForm):
    class Meta:
        model = Firewalls
        fields = '__all__'

class FirewallsMarcasForms(forms.ModelForm):
    class Meta:
        model = FirewallsMarcas
        fields = '__all__'

class HerramientaDeDesarrolloForms(forms.ModelForm):
    class Meta:
        model = HerramientaDeDesarrollo
        fields = '__all__'

class ImpresorasForms(forms.ModelForm):
    class Meta:
        model = Impresoras
        fields = '__all__'

class ImpresorasMarcasForms(forms.ModelForm):
    class Meta:
        model = ImpresorasMarcas
        fields = '__all__'

class ProyectoresForms(forms.ModelForm):
    class Meta:
        model = Proyectores
        fields = '__all__'

class ProyectoresMarcasForms(forms.ModelForm):
    class Meta:
        model = ProyectoresMarcas
        fields = '__all__'

class RoutersForms(forms.ModelForm):
    class Meta:
        model = Routers
        fields = '__all__'

class RoutersForms(forms.ModelForm):
    class Meta:
        model = Routers
        fields = '__all__'

class SecretariasForms(forms.ModelForm):
    class Meta:
        model = Secretarias
        fields = '__all__'

class SistemaDeInformacionMovilForms(forms.ModelForm):
    class Meta:
        model = SistemaDeInformacionMovil
        fields = '__all__'


class SistemaInformacionMovilNombresForms(forms.ModelForm):
    class Meta:
        model = SistemaInformacionMovilNombres
        fields = '__all__'

class SistemasInformacionForms(forms.ModelForm):
    class Meta:
        model = SistemasInformacion
        fields = '__all__'

class SistemasInformacionNombresForms(forms.ModelForm):
    class Meta:
        model = SistemasInformacionNombres
        fields = '__all__'

class SitesForms(forms.ModelForm):
    class Meta:
        model = Sites
        fields = '__all__'

class UsuariosForms(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

class LoginForm(forms.Form):
    email = forms.CharField(label='Email')
    contrasenia = forms.CharField(label='Contraseña', widget=forms.PasswordInput)