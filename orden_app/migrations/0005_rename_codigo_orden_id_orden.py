# Generated by Django 5.1.3 on 2024-12-03 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orden_app', '0004_orden_id_gato'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden',
            old_name='codigo',
            new_name='id_orden',
        ),
    ]
