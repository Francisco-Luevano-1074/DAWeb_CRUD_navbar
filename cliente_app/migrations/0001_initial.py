# Generated by Django 5.1.3 on 2024-11-28 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo', models.IntegerField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=100)),
                ('no_telefono', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('orden', models.CharField(max_length=100)),
                ('mesa', models.CharField(max_length=255)),
            ],
        ),
    ]
