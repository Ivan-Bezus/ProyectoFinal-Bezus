# Generated by Django 4.1.3 on 2022-12-15 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp1', '0007_rename_reserv_gain_booking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Reserva', 'verbose_name_plural': 'Reservas'},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='date_registered',
        ),
    ]
