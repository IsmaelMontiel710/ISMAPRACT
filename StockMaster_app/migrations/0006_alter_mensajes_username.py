# Generated by Django 4.2.5 on 2023-09-30 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockMaster_app', '0005_rename_nusuario_mensajes_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]
