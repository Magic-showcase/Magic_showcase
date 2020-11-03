from django.db import models
from django.contrib.auth.models import User
class Vendedor(models.Model):
    Usuario=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    Foto=models.ImageField(upload_to='Online_garage_store')
    Edad=models.IntegerField()
    Sexo=models.CharField(max_length=50)
    Email=models.EmailField()
    Domicilio=models.CharField(max_length=70)

class User_Product(models.Model):
    Vendedor=models.ForeignKey(Vendedor,on_delete=models.DO_NOTHING,default=None)
    Nombre=models.CharField(max_length=50)
    Seccion=models.CharField(max_length=50)
    Contenido=models.CharField(max_length=50)
    Precio=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,)
    #guardar sitio adecuado de imagen upload_to
    Imagen=models.ImageField(upload_to='Online_garage_store')
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Producto_usuario'
        verbose_name_plural='Productos_usuario'
    
    def _str_(self):
        return self.Nombre

class User_Venta_descrip(models.Model):
    Vendedor=models.ForeignKey(Vendedor,on_delete=models.DO_NOTHING,default=None)
    Cliente=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    Producto=models.ForeignKey(User_Product,on_delete=models.DO_NOTHING,default=None)
    Cantidad=models.IntegerField()
    Precio_unitario=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    class Meta:
        verbose_name='Usuario_Venta_descrip'
        verbose_name_plural='Usuario_Venta_descrip'


class User_Venta(models.Model):
    Venta_desc=models.ForeignKey(User_Venta_descrip,on_delete=models.DO_NOTHING)
    Vendedor=models.ForeignKey(Vendedor,on_delete=models.DO_NOTHING,default=None)
    Cliente=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    subtotal=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Precio_IVA=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Costo_total=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    class Meta:
       verbose_name='Venta_usuario'
       verbose_name_plural='Ventas_usuario'

class User_Envio(models.Model):
    Vendedor=models.ForeignKey(Vendedor,on_delete=models.DO_NOTHING,default=None)
    Cliente=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    Venta=models.ForeignKey(User_Venta,on_delete=models.DO_NOTHING,default=None)
    Address=models.TextField()
    Fecha=models.DateField()
    Entregado=models.BooleanField()
    class Meta:
        verbose_name='Envio_usuario'
        verbose_name_plural='Envios_usuario'
