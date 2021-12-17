from django.db import models

# Create your models here.

class categoria(models.Model):
	nombre = models.CharField(max_length = 30)
	descripcion = models.CharField(max_length = 100000, null = False)

	def __str__(self):
		return self.nombre


class post(models.Model):
	nombre = models.CharField(max_length = 100000)
	descripcion = models.CharField(max_length = 100000, null = False)
	imagen = models.ImageField(upload_to = 'imagenes_post', null = True)

	def __str__(self):
		return self.nombre