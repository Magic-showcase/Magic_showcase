from django.shortcuts import render
from .models import Tutoriales
# Create your views here.

def Tutorial(request):

    tutorial = Tutoriales.objects.all()

    return render(request,'Centro/Tutoriales.html',{"tutorial":tutorial})