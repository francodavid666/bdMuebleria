# Generated by Django 4.1.7 on 2023-05-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_propiedad_model',
            name='direccion2',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
