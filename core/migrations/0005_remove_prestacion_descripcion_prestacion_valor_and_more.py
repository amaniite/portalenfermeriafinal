# Generated by Django 4.1.3 on 2022-12-13 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_profesional_comuna_alter_profesional_region"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prestacion",
            name="descripcion",
        ),
        migrations.AddField(
            model_name="prestacion",
            name="valor",
            field=models.DecimalField(
                blank=True, decimal_places=0, max_digits=12, null=True
            ),
        ),
        migrations.AlterField(
            model_name="profesional",
            name="descripcion",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
