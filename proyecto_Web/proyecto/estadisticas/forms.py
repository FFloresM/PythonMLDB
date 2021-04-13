from django.db.models import fields
from django.forms import ModelForm
from .models import Juez

class JuezModelForm(ModelForm):
    class Meta:
        model = Juez
        fields = ['nombre', 'apellido_paterno', 'genero']
