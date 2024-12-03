# Generated by Django 5.1.3 on 2024-11-26 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('productos', models.CharField(max_length=255)),
                ('mesa', models.CharField(max_length=100)),
                ('nom_cliente', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('costo', models.CharField(max_length=100)),
                ('hora', models.DateField(max_length=6)),
            ],
        ),
    ]
