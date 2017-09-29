from __future__ import unicode_literals
from django.db import models

# Create your models here.

class habitacion(models.Model):
	tipo_habitacion = (
		('0', 'sencillas'),
		('1', 'dobles'),
		)
	tipo = models.CharField(
	max_length=1,
	choices = tipo_habitacion,
	default = '0',
	)
	descripcion = models.CharField(max_length = 150)
	numero = models.IntegerField()
	ocupado = models.BooleanField(default=False)
	fecha = models.DateTimeField(auto_now_add = True)

def __str__(self):
		return '%s %s' % (self.numero,self.tipo,self.ocupado,self.descripcion)

class cliente(models.Model):
	habitacion = models.ForeignKey(habitacion)
	nombre = models.CharField(max_length = 150)
	dpi = models.CharField(max_length = 20)
	fecha_ingreso = models.DateTimeField(auto_now_add = True)
	fecha_egreso = models.DateTimeField()

def __str__(self):
		return '%s %s' % (self.nombre,self.dpi,self.habitacion)