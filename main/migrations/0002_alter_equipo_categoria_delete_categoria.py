# Generated by Django 5.1 on 2024-08-16 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='categoria',
            field=models.CharField(choices=[('Ski', 'Ski'), ('Botas', 'Botas'), ('Trineo', 'Trineo'), ('Snow Board', 'Snow Board'), ('Otros', 'Otros')], max_length=15),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
