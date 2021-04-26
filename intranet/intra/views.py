from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import OficioEntrada
from django.urls import reverse, reverse_lazy
from .forms import OficioEntradaForm

@login_required()
def index(request):
    var = "hola mundo"
    return render(request, "intra/base.html", {"hola": var})

def upload_file(request):
    if request.method == 'POST':
        form = OficioEntradaForm(request.POST, request.FILES)
        if form.is_valid():
            #oficioE = form.save(commit=False)
            #oficioE.foto = request.FILES['foto']
            #form.archivo = request.FILES['archivo']
            form.save()
            return render(request,'intra/base.html')
    else:
        form = OficioEntradaForm()
    return render(request, 'intra/oficioentrada_form.html', {'form': form})

#class OficioEntradaCreateView(CreateView):
#    model = OficioEntrada
#    form_class = OficioEntradaForm(request.POST, request.FILE)
#    success_url = reverse_lazy('intra:index')
    

    