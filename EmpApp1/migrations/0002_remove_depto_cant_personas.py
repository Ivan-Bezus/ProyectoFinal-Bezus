# Generated by Django 4.1.2 on 2022-11-12 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depto',
            name='cant_personas',
        ),
    ]