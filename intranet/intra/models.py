from django.db import models
from django.contrib.auth.models import User

class OficioEntrada(models.Model):
    fecha_oficio = models.DateField()
    fecha_recepcion = models.DateField(auto_now=True)
    numero_oficio = models.CharField(max_length=10)
    referencia = models.CharField(max_length=40)
    observacion = models.CharField(max_length=140)
    archivo = models.FileField(upload_to='OficiosEntrada', null=False)
    creado_por = User
    institucion = models.ForeignKey('Institucion', on_delete=models.SET_NULL, null=True)

class OficioSalida(models.Model):
    #correlativo es clave primaria (id)
    formaEnvio = [
        ('correo electrónico', 'correo electrónico'),
        ('correos de chile', 'correos de chile'),
        ('por mano', 'por mano'),
    ]
    ESTADOS = [
        ('pendiente','pendiente'),
        ('enviado','enviado'),
        ('anulado', 'anulado'),
    ]
    fecha_oficio = models.DateField(auto_now=True)
    rit = models.CharField(max_length=10)
    referencia = models.CharField(max_length=20)
    comuna = models.CharField(max_length=20)
    fecha_envio = models.DateField()
    codigo_envio = models.IntegerField()
    forma_envio = models.CharField(choices=formaEnvio, max_length=20)
    creado_por = User
    estado = models.CharField(choices=ESTADOS, max_length=12)
    archivo = models.FileField(upload_to='OficiosSalida', null=True, blank=True)
    institucion = models.ForeignKey('Institucion', on_delete=models.SET_NULL, null=True)

class Institucion(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Instituciones"