from django.urls import path
from Nucleo.views import Home,Contactos
#importar settings para usar 2 variables
from django.conf import settings
#importar archivos static
from django.conf.urls.static import static

urlpatterns = [
    path('',Home, name="Home"),
    path('Contactos/',Contactos,name="Contactos"),
]

#Agregar Urls
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)