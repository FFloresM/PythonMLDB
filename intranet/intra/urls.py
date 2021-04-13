from django.urls import path

from . import views

app_name = 'intra'

urlpatterns = [
    path('', views.index, name='index'),
    path('entrada/', views.OficioEntradaCreateView.as_view(), name='formulario-entrada'),
]