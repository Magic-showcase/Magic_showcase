from django.shortcuts import render
from Tutorial.models import Tutorials,Categoria
from Usuario.models import Users
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
def Tutor(request):
    tuto = Tutorials.objects.all()

    return render(request,'Centro/Tutorial.html',{"tuto":tuto})