from django.shortcuts import render
from django.http import HttpResponse 
from .models import Tutoriales
# Create your views here.

def Tutoriales(request):
    tutorial=Tutoriales.objects.all()
    return render(request,'Centro/Tutoriales.html',{"tutorial":tutorial})