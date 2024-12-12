from django.db import models

# Create your models here.

class Agenda(models.Model):
    Id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    usuario = models.CharField(max_length=50)
    gmail = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=40)

class Suplemento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='./static/css/img')

    def __str__(self):
        return self.nombre

class Food(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField()
    grams = models.IntegerField()

    def __str__(self):
        return self.name