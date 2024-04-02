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
        self.fields['Dependencia'].queryset = Dependencias.objects.values_list('nombre_dependencia', flat=True)  # Reemplaza 'nombre_dependencia' con el campo que deseas mostrar
        self.fields['id_marca'].queryset = ConmutadoresMarcas.objects.values_list('marca_conmutador', flat=True)  # Reemplaza 'marca_conmutador' con el campo que deseas mostrar