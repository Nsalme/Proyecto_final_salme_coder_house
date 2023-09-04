from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10, choices=[('M', 'Macho'), ('H', 'Hembra')])
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='animales/', null=True, blank=True)

class Personal(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    contacto = models.EmailField()
    imagen = models.ImageField(upload_to='personal/', null=True, blank=True)
# Modelo para representar formularios en el zoológico
class Formulario(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    archivo = models.FileField(upload_to='formularios/')

    def __str__(self):
        return self.titulo

# Modelo para representar eventos en el zoológico
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='evento/', null=True, blank=True)

    def __str__(self):
        return self.titulo