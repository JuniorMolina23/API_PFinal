# Generated by Django 4.1.3 on 2022-11-24 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_proyecto_final', '0004_detalletemperatura'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalletemperatura',
            old_name='t_almacen_id',
            new_name='almacen_id',
        ),
    ]
