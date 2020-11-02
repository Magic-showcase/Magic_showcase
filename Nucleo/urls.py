from django.urls import path
from Nucleo.views import Home,Tutoriales,Preguntas,Contactos,Memberships
#importar settings para usar 2 variables
from django.conf import settings
#importar archivos static
from django.conf.urls.static import static

urlpatterns = [
    path('',Home, name="Home"),
    path('Tutoriales/',Tutoriales,name="Tutoriales"),
    path('Preguntas/',Preguntas,name="Preguntas"),
    path('Contactos/',Contactos,name="Contactos"),
    path('Memberships/',Memberships,name="Memberships"),
]

#Agregar Urls
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
