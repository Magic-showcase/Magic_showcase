from django.db import models
#importar clase user

from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    Nombre=models.CharField(max_length=50)
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
    
    def _str_(self):
        return self.Nombre


class POST(models.Model):
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
        verbose_name='POST'
        verbose_name_plural='POSTS'
    
    def _str_(self):
        return self.Titulo
