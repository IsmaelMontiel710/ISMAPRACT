# Generated by Django 4.2.5 on 2023-09-30 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockMaster_app', '0004_mensajes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensajes',
            old_name='nusuario',
            new_name='username',
        ),
    ]
