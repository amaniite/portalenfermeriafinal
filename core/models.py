from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comuna(models.Model):
    region = models.ForeignKey('Region', db_column='id_region', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
         return f'{self.nombre}'


        
class Region(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
         return f'{self.nombre}'


class Direccion(models.Model):
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    calle = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
         return f'{self.calle}'



class Prestacion(models.Model):
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    nombre = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
         return f'{self.nombre}'


class Paciente(models.Model):
    rut_paciente = models.CharField(primary_key=True, max_length=10)
    prestacion = models.ForeignKey('Prestacion', models.DO_NOTHING, db_column='id_prestacion')
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    primer_nombre = models.CharField(max_length=50, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    primer_apellido = models.CharField(max_length=50, blank=True, null=True)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    correo_electronico = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    patologia = models.CharField(max_length=100, blank=True, null=True)
    alergia = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
         return f'{self.primer_nombre} {self.primer_apellido} {self.segundo_apellido}'

class Profesional(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    rut_profesional = models.CharField(primary_key=True, max_length=10)
    primer_nombre = models.CharField(max_length=50, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    primer_apellido = models.CharField(max_length=50, blank=True, null=True)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    region = models.ForeignKey('Region',blank=True, null=True, db_column='id_region', on_delete=models.CASCADE)
    comuna = models.ForeignKey('Comuna', blank=True, null=True, db_column='id_comuna', on_delete=models.CASCADE)
    prestacion = models.ForeignKey('Prestacion',blank=True, null=True, db_column='id_prestacion', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    correo_electronico = models.CharField(max_length=50, blank=True, null=True)
    numero_sis = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    telefono = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    descripcion = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
         return f'{self.primer_nombre} {self.primer_apellido} {self.segundo_apellido}'



class Valoracion(models.Model):
    rut_profesional = models.ForeignKey(Profesional, models.DO_NOTHING, db_column='rut_profesional', blank=True, null=True)
    rut_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='rut_paciente', blank=True, null=True)
    puntuacion = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
         return f'{self.puntuacion}'
