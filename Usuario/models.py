from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Photo = models.ImageField(upload_to='Usuario',blank=True,null=True)
    LATAM_ISO_COUNTIES =[
        ('mex','México'),
        ('usa','United States'),
        ('can','Canada'),
        ('bra','Brazil'),
    ]
    country = models.CharField(choices=LATAM_ISO_COUNTIES,max_length=60,null=True) 

    birth = models.DateField(blank=True,null=False)
    bio = models.TextField(blank=True,null=True)
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)




    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'
    def __str__(self):
        return str(self.user.username)