# Generated by Django 4.2.4 on 2023-08-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectorapp', '0002_consultaproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultaproducto',
            name='total_consultas',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
