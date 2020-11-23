from django.db import models

# importar clase de usuario
from django.contrib.auth.models import User

# create your models here

class Categoria(models.Model):
    Nombre=models.CharField(max_length=50)
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
    
    def _str_(self):
        return self.Nombre


class Tutoriales(models.Model):
    Titulo=models.CharField(max_length=50)
    Contenido=models.TextField()
    #guardar sitio adecuado de imagen upload_to
    Imagen=models.ImageField(upload_to='Blog', null=True, blank=True)
    #si un autor se va se borra el post
    Autor=models.ForeignKey(User,on_delete=models.CASCADE)
    #relacion entre post y categoria
    Categorias=models.ManyToManyField(Categoria)
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Tutorial'
        verbose_name_plural='Tutoriales'
    
    def _str_(self):
        return self.Titulo