# Generated by Django 5.1 on 2024-08-17 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_equipo_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='precio',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
