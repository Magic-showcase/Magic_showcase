from django.urls import path
from Control_Vi.views import Servicio_Control

urlpatterns = [
    path('Servicio_Control/',Servicio_Control,name="Servicio_Control"),
]
