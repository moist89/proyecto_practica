from django.db import models

class cliente(models.Model):
	nombre =	models.CharField(max_length=200)
	apellido=	models.CharField(max_length=200)	
	estatus=	models.BooleanField(default=True)
	def __unicode__(self):
		nombreCompleto="%s%s" %(self.nombre,self.apellido)
		return nombreCompleto

class producto(models.Model):
	nombre=			models.CharField(max_length=200)
	descripcion=	models.TextField(max_length=300)
	estatus=		models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre