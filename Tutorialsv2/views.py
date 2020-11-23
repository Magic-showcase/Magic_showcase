from django.shortcuts import render
from .models import Tutoriales
from .models import Categoria
# Create your views here.

def Tutorials(request):

    cate = Categoria.objects.all()
    tuto = Tutoriales.objects.all()

    return render(request,'Centro/Tutoriales.html', {"tuto":tuto,"cate":cate})