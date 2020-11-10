from django.http import HttpResponse 
#Importar shortcuts
from django.shortcuts import render
#Importar libreria serial 
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def Servicio_Control(request):
    return render(request,'Central/Servicio_Control.html')