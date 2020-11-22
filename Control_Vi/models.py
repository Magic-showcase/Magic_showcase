from django.db import models

from Usuario.models import Users
#importar cloudinary
from cloudinary.models import CloudinaryField
# Create your models here.

class Item(models.Model):
    Usuario = models.ForeignKey(Users,on_delete=models.CASCADE,default=None)
    Nombre=models.CharField(max_length=50)
    Seccion=models.CharField(max_length=50)
    Contenido=models.CharField(max_length=50)
    Precio=models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    #guardar sitio adecuado de imagen upload_to
    #Imagen=models.ImageField(upload_to='Tienda')
    Imagen =  CloudinaryField('image')
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Item'
        verbose_name_plural='Items'
    
    def __str__(self):
        return self.Nombre

class Showcase(models.Model):
    Usuario = models.ForeignKey(Users,on_delete=models.CASCADE,default=None)
    Nombrevi = models.CharField(max_length=50)
    Seccion=models.CharField(max_length=50)
    Slot1 = models.ForeignKey(Item,on_delete=models.DO_NOTHING,related_name='Slot1',default=None)
    Slot2 = models.ForeignKey(Item,on_delete=models.DO_NOTHING,related_name='Slot2',default=None)
    Slot3 = models.ForeignKey(Item,on_delete=models.DO_NOTHING,related_name='Slot3',default=None)
    Slot4 = models.ForeignKey(Item,on_delete=models.DO_NOTHING,related_name='Slot4',default=None)
    Slot5 = models.ForeignKey(Item,on_delete=models.DO_NOTHING,related_name='Slot5',default=None)
    Slot6 = models.ForeignKey(Item,on_delete=models.DO_NOTHING,related_name='Slot6',default=None)
    Slot7 = models.ForeignKey(Item,on_delete=models.DO_NOTHING,related_name='Slot7',default=None)
    Slot8 = models.ForeignKey(Item,on_delete=models.DO_NOTHING,related_name='Slot8',default=None)
    Slot9 = models.ForeignKey(Item,on_delete=models.DO_NOTHING,related_name='Slot9',default=None)
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Showcase'
        verbose_name_plural='Showcases'
    
    def __str__(self):
        return self.Nombrevi


        

