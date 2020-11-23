from django.shortcuts import render
from .models import Tutoriales
# Create your views here.

def Tutorials(request):


    return render(request,'Centro/Tutoriales.html')