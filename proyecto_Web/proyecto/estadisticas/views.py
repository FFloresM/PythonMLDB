from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .forms import JuezModelForm
from .models import Juez
from django.urls import reverse

def index(request):
    return render(request, 'estadisticas/base.html')

class CrearJuez(CreateView):
    model = Juez
    form_class = JuezModelForm

    def get_success_url(self):
	    return reverse('estadisticas:index')



