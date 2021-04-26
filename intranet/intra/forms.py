from django.forms import TextInput, Select, NumberInput, ModelForm, FileInput
from .models import OficioEntrada

class OficioEntradaForm(ModelForm):
    class Meta:
        model = OficioEntrada
        fields = ['fecha_oficio', 'numero_oficio', 'referencia', 'observacion', 'institucion', 'archivo']
        widgets = {
            'fecha_oficio': TextInput(attrs={'class': 'form-control', 'placeholder':"fecha oficio de entrada"}),
            'numero_oficio': NumberInput(attrs={'class': 'form-control', 'placeholder':"numero de oficio"}),
            'referencia': TextInput(attrs={'class': 'form-control', 'placeholder':"asunto del oficio"}),
            'observacion': TextInput(attrs={'class': 'form-control', 'placeholder':"observación"}),
            'institucion': Select(attrs={'class': 'form-control', 'placeholder':"institución"}),
            'archivo': FileInput(attrs={'class': 'form-control'}),
        }