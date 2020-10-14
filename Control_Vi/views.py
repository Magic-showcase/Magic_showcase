from django.http import HttpResponse 
#Importar shortcuts
from django.shortcuts import render
#Importar libreria serial 


# Create your views here.
def Servicio_Control(request):
    return render(request,'Central/Servicio_Control.html')