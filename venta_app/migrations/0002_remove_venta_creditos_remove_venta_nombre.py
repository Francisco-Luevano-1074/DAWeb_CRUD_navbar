# Generated by Django 5.1 on 2024-11-12 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='creditos',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='nombre',
        ),
    ]
