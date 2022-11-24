from django.db import models

# Create your models here.

class Depto (models.Model):
    cobro_x_día = models.CharField(max_length=20)
    fecha_entrada = models.DateField(max_length=30) 
    fecha_salida = models.DateField(max_length=30)
    
    def __str__(self):
        return f'{self.fecha_entrada} - {self.fecha_salida} - {self.cobro_x_día}'

class Inquilino (models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.dni} - {self.email}'

class Ganancia (models.Model):
    precio_x_dia = models.CharField(max_length=30)
    costo_gestion = models.CharField(max_length= 30)
    costo_mant = models.CharField(max_length=30)
    costo_limpieza = models.CharField(max_length=30)
    ganancia = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.precio_x_dia} - {self.costo_mant} - {self.costo_mant} - {self.costo_limpieza} - {self.ganancia}'