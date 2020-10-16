from django.http import HttpResponse 
#Importar shortcuts
from django.shortcuts import render



def Home(request):
    return render(request,'Central/Home.html')

def Tutoriales(request):
    return render(request,'Central/Tutoriales.html')

def Blog(request):
    return render(request,'Central/Blog.html')

def Preguntas(request):
    return render(request,'Central/Preguntas.html')

def Contactos(request):
    return render(request,'Central/Contactos.html')