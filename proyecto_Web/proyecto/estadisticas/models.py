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