from django.urls import path
from Control_Vi.views import Servicio_Control, Itemcre

urlpatterns = [
    path('Servicio_Control/',Servicio_Control,name="Servicio_Control"),
    path('Crear_Item/',Itemcre,name='Crear_Item'),
]
