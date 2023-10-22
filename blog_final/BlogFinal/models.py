from django.db import models

class Usuario(models.Model):
    nombre=models.CharField(max_length=40)
    contraseña=models.CharField(max_length=40)

class Blogs(models.Model):
    blog=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=40)
    