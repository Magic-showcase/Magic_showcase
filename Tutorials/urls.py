from django.urls import path
from Tutorials.views import Tutoriales
from django.conf import Settings
from django.conf.urls.static import static

urlpatterns = [
        path('Tutoriales/',Tutoriales,name="Tutoriales"),
]
