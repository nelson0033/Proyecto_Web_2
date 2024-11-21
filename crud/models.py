from django.db import models

# Create your models here.

class VideojuegoRetro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_lanzamiento = models.DateField()
    genero = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=100)
    portada = models.FileField(upload_to="videojuegos/")

    def __str__(self):
        return self.titulo
