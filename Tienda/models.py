from django.db import models

class Producto(models.Model):
    Nombre=models.CharField(max_length=50)
    Seccion=models.CharField(max_length=50)
    Contenido=models.CharField(max_length=50)
    Precio=models.IntegerField()
    #guardar sitio adecuado de imagen upload_to
    Imagen=models.ImageField(upload_to='Tienda')
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
    
    def _str_(self):
        return self.Nombre
