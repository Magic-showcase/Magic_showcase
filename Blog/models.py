from django.db import models
#importar clase user
from Usuario.models import Users
#importar cloudinary
from cloudinary.models import CloudinaryField
#Create your models here.

class Categoria(models.Model):
    Nombre=models.CharField(max_length=50)
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
    
    def __str__(self):
        return str(self.Nombre)


class POST(models.Model):
    Titulo=models.CharField(max_length=50)
    Contenido=models.TextField()
    #guardar sitio adecuado de imagen upload_to
    #Imagen=models.ImageField(upload_to='Blog', null=True, blank=True)
    Imagen = CloudinaryField('image')
    #si un autor se va se borra el post
    Autor=models.ForeignKey(Users,on_delete=models.CASCADE)
    #relacion entre post y categoria
    Categorias=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='POST'
        verbose_name_plural='POSTS'
    
    def __str__(self):
        return str(self.Titulo)
