# Generated by Django 5.0.2 on 2024-06-06 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesion', '0006_alter_iniciosesion_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iniciosesion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sesion.registrarse', to_field='correo'),
        ),
    ]
