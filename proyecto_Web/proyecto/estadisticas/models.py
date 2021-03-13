from django.db import models

class Juez(models.Model):
    genero_choices = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    nombre = models.CharField(max_length=15, null=True)
    apellido_paterno = models.CharField(max_length=15, null=False)
    genero = models.CharField(max_length=10, choices=genero_choices, default='M')

    def __str__(self):
        return self.apellido_paterno

    class Meta:
        verbose_name_plural = 'Jueces'

class TipoDeAudiencia(models.Model):
    tipo_audiencia_choices = [
        ('preparatoria', "A. PREPARATORIA"),
        ('juicio', 'A. DE JUICIO'),
        ('especial', 'ESPECIAL / INCIDENTAL / UNICA'),
        ('continuacion juicio', 'CONTINUACIÓN JUICIO'),
        ('continuacion preparatoria', 'CONTINUACIÓN PREPARATORIA'),
        ('continuacion especial','CONTINUACION ESPECIAL/INCIDENTAL'),
        ('inmediata','AUDIENCIA INMEDIATA'),
    ]
    tipo = models.CharField(max_length=40, choices=tipo_audiencia_choices)
    bloques = models.IntegerField(default=0) #numero de bloques
    duracion_real = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.tipo