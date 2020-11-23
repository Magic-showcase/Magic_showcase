from django.urls import path
from Tutorialsv2.views import Tutoriales
from django.conf import Settings
from django.conf.urls.static import static

urlpatterns = [
        path('Tutoriales/',Tutoriales,name="Tutoriales"),
]
