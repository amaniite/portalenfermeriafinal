# Generated by Django 4.1.3 on 2022-12-13 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comuna",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Paciente",
            fields=[
                (
                    "rut_paciente",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                (
                    "primer_nombre",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "segundo_nombre",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "primer_apellido",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "segundo_apellido",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "correo_electronico",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "telefono",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=12, null=True
                    ),
                ),
                ("patologia", models.CharField(blank=True, max_length=100, null=True)),
                ("alergia", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "comuna",
                    models.ForeignKey(
                        db_column="id_comuna",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.comuna",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Prestacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=50, null=True)),
                ("descripcion", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "comuna",
                    models.ForeignKey(
                        db_column="id_comuna",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.comuna",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profesional",
            fields=[
                (
                    "rut_profesional",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                (
                    "primer_nombre",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "segundo_nombre",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "primer_apellido",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "segundo_apellido",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "correo_electronico",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "numero_sis",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=15, null=True
                    ),
                ),
                (
                    "telefono",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=12, null=True
                    ),
                ),
                (
                    "descripcion",
                    models.TextField(blank=True, max_length=100, null=True),
                ),
                (
                    "comuna",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.comuna",
                    ),
                ),
                (
                    "prestacion",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.prestacion",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Valoracion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("puntuacion", models.IntegerField()),
                (
                    "descripcion",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "rut_paciente",
                    models.ForeignKey(
                        blank=True,
                        db_column="rut_paciente",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.paciente",
                    ),
                ),
                (
                    "rut_profesional",
                    models.ForeignKey(
                        blank=True,
                        db_column="rut_profesional",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.profesional",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="paciente",
            name="prestacion",
            field=models.ForeignKey(
                db_column="id_prestacion",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="core.prestacion",
            ),
        ),
        migrations.CreateModel(
            name="Direccion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("calle", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "comuna",
                    models.ForeignKey(
                        db_column="id_comuna",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.comuna",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="comuna",
            name="region",
            field=models.ForeignKey(
                db_column="id_region",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.region",
            ),
        ),
    ]
