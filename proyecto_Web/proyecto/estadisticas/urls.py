from django.urls import path
from .views import CrearJuez

from . import views

app_name = 'estadisticas'

urlpatterns = [
    path('', views.index, name='index'),
    path('juez/nuevo', CrearJuez.as_view(), name="crear-juez"),
]
