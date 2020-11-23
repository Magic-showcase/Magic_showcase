from django.urls import path
from Control_Vi.views import Servicio_Control, Itemcre, Vicre

urlpatterns = [
    path('Servicio_Control/',Servicio_Control,name="Servicio_Control"),
    path('Crear_Item/',Itemcre,name='Crear_Item'),
    path('Crear_Vitrina/',Vicre,name='Crear_Vitrina'),
]
