# Generated by Django 5.1.3 on 2024-11-26 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gato',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('edad', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=100)),
                ('caracteristica', models.CharField(max_length=255)),
            ],
        ),
    ]