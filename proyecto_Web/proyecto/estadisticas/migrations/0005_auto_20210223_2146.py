# Generated by Django 3.1.7 on 2021-02-23 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0004_auto_20210223_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipodeaudiencia',
            old_name='duracion',
            new_name='bloques',
        ),
        migrations.AlterField(
            model_name='tipodeaudiencia',
            name='duracion_real',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
