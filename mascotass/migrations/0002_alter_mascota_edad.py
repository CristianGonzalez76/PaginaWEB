# Generated by Django 4.0.3 on 2022-04-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad',
            field=models.CharField(max_length=30),
        ),
    ]
