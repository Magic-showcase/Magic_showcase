from django.db import models

# importar clase de usuario
from Usuario.models import Users
from cloudinary.models import CloudinaryField

# create your models here

class Categoria(models.Model):
    Nombre=models.CharField(max_length=50)
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
    
    def __str__(self):
        return self.Nombre


class Tutoriales(models.Model):
    Titulo=models.CharField(max_length=50)
    Contenido=models.TextField()
    #guardar sitio adecuado de imagen upload_to
    Imagen = CloudinaryField('image')
    #si un autor se va se borra el post
    Autor=models.ForeignKey(Users,on_delete=models.CASCADE)
    #relacion entre post y categoria
    Categorias=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Tutorial'
        verbose_name_plural='Tutoriales'
    
    def __str__(self):
        return self.Titulo