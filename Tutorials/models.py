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