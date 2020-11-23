from django.urls import path
from . import views
#importar settings para usar 2 variables
from django.conf import settings
#importar archivos static
from django.conf.urls.static import static

urlpatterns = [
    path('Tutorial/',views.Tutor,name="Tutorial"),
   path('Tucate/<int:Categoria_id>/',views.Tutofilt,name="Tucate"),
]