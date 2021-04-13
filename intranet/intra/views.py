from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import OficioEntrada
from django.urls import reverse, reverse_lazy

@login_required()
def index(request):
    var = "hola mundo"
    return render(request, "intra/base.html", {"hola": var})

class OficioEntradaCreateView(CreateView):
    model = OficioEntrada
    fields = ['fecha_oficio', 'numero_oficio', 'referencia', 'observacion', 'institucion']
    success_url = reverse_lazy('intra:index')
    

    