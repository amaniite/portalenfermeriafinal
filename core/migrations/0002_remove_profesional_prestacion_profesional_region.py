# Generated by Django 4.1.3 on 2022-12-13 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profesional",
            name="prestacion",
        ),
        migrations.AddField(
            model_name="profesional",
            name="region",
            field=models.OneToOneField(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="core.region"
            ),
        ),
    ]
