# Generated by Django 4.1.3 on 2022-12-13 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_remove_prestacion_descripcion_prestacion_valor_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prestacion",
            name="valor",
        ),
        migrations.AddField(
            model_name="profesional",
            name="valor",
            field=models.DecimalField(
                blank=True, decimal_places=0, max_digits=12, null=True
            ),
        ),
    ]