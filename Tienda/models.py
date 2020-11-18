from django.db import models
from Usuario.models import Users
from cloudinary.models import CloudinaryField
class Producto(models.Model):
    Nombre=models.CharField(max_length=50)
    Seccion=models.CharField(max_length=50)
    Contenido=models.CharField(max_length=50)
    Precio=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,)
    #guardar sitio adecuado de imagen upload_to
    #Imagen=models.ImageField(upload_to='Tienda')
    Imagen =  CloudinaryField('image')
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
    
    def __str__(self):
        return self.Nombre
        
class Venta(models.Model):
    Cliente=models.ForeignKey(Users,on_delete=models.DO_NOTHING,default=None)
    Producto=models.ForeignKey(Producto,on_delete=models.DO_NOTHING,default=None)
    Precio_unitario=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Cantidad=models.IntegerField()
    subtotal=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Precio_IVA=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Costo_total=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    class Meta:
       verbose_name='Venta'
       verbose_name_plural='Ventas'

class Envio(models.Model):
    Cliente=models.ForeignKey(Users,on_delete=models.DO_NOTHING,default=None)
    Venta=models.ForeignKey(Venta,on_delete=models.DO_NOTHING,default=None)
    Address=models.TextField()
    Fecha=models.DateField()
    Entregado=models.BooleanField()
    class Meta:
        verbose_name='Envio'
        verbose_name_plural='Envios'