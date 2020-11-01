from django.db import models
from django.contrib.auth.models import User
class Producto(models.Model):
    Nombre=models.CharField(max_length=50)
    Seccion=models.CharField(max_length=50)
    Contenido=models.CharField(max_length=50)
    Precio=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,)
    #guardar sitio adecuado de imagen upload_to
    Imagen=models.ImageField(upload_to='Tienda')
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
    
    def _str_(self):
        return self.Nombre

class Venta_descrip(models.Model):
    Cliente=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    Producto=models.ManyToManyField(Producto)
    Cantidad=models.IntegerField()
    Precio_unitario=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    class Meta:
        verbose_name='Venta_descrip'
        verbose_name_plural='Venta_descrip'


class Venta(models.Model):
    Venta_desc=models.ForeignKey(Venta_descrip,on_delete=models.DO_NOTHING)
    Cliente=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    subtotal=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Precio_IVA=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Costo_total=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    class Meta:
       verbose_name='Venta'
       verbose_name_plural='Ventas'

class Envio(models.Model):
    Cliente=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    Venta=models.ForeignKey(Venta,on_delete=models.DO_NOTHING,default=None)
    Fecha=models.DateField()
    Entregado=models.BooleanField()
    class Meta:
        verbose_name='Envio'
        verbose_name_plural='Envios'