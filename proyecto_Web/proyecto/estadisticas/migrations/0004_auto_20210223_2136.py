# Generated by Django 3.1.7 on 2021-02-23 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0003_tipodeaudiencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipodeaudiencia',
            name='duracion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tipodeaudiencia',
            name='duracion_real',
            field=models.DateTimeField(null=True),
        ),
    ]
