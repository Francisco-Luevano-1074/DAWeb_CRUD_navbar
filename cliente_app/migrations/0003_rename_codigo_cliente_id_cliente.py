# Generated by Django 5.1.3 on 2024-12-03 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_app', '0002_remove_cliente_mesa_remove_cliente_orden_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='codigo',
            new_name='id_cliente',
        ),
    ]
