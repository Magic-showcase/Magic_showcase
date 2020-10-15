from django.urls import path
from Tienda.views import Tienda

urlpatterns = [
    path('Tienda/',Tienda,name="Tienda"),
]
