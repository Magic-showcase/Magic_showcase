from django.urls import path
from Tutorialsv2.views import Tutorials

urlpatterns = [
        path('Tutoriales/',Tutorials,name="Tutoriales"),
]
