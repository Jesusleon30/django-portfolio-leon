from django.db import models

# Create your models here.
#  dentro de los m,odels siempre va air las tablas

class Immagine(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.ImageField(upload_to='images/', blank=True, null=True) # esto seria que te da la opcion de poder subir la imagen en blanco si esque lo decea el cliente
    img_url_full = models.URLField(blank=True, null=True)
    