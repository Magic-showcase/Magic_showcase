from django.urls import path
from Ventas.views import Home,Tienda,Tutoriales,Blog,Preguntas,Contactos

urlpatterns = [
    path('',Home, name="Home"),
    path('Tienda/',Tienda,name="Tienda"),
    path('Tutoriales/',Tutoriales,name="Tutoriales"),
    path('Blog/',Blog,name="Blog"),
    path('Preguntas/',Preguntas,name="Preguntas"),
    path('Contactos/',Contactos,name="Contactos"),
]
