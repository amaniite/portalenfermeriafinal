# Generated by Django 4.1.3 on 2022-12-13 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_profesional_prestacion_profesional_region"),
    ]

    operations = [
        migrations.AddField(
            model_name="profesional",
            name="prestacion",
            field=models.ForeignKey(
                blank=True,
                db_column="id_prestacion",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.prestacion",
            ),
        ),
    ]
