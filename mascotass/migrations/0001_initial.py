# Generated by Django 4.0.3 on 2022-04-01 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('correlativo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('fotografia', models.ImageField(upload_to='')),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=12)),
                ('fecha_de_rescate', models.DateField()),
                ('estado', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=25)),
                ('enfermedad', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'mascota',
                'verbose_name_plural': 'mascotas',
            },
        ),
    ]
