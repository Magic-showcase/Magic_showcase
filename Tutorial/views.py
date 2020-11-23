from django.shortcuts import render
from Tutorial.models import Tutorials,Categoria
from Usuario.models import Users
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
def Tutor(request):
    tuto = Tutorials.objects.all()
    catego = Categoria.objects.all()
    return render(request,'Centro/Tutorial.html',{"tuto":tuto,"catego":catego})

def Tutofilt(request, Categoria_id):
    categotias = Categoria.objects.get(id= Categoria_id)
    cate = Categoria.objects.all()
    Tuto = Tutorials.objects.filter(Categorias=categotias)

    return render(request,'Centro/Tutcateg.html',{"Tuto":Tuto,"categotias":categotias,"cate":cate})

