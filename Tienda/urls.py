from django.urls import path
from . import views
#importar settings para usar 2 variables
from django.conf import settings
#importar archivos static
from django.conf.urls.static import static

urlpatterns = [
    path('Tienda/',views.Tienda,name="Tienda"),
    path('Comprar/',views.Compra,name="Comprar"),
]

