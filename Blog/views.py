from django.shortcuts import render
from Blog.models import POST,Categoria
from Usuario.models import Users
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
def Blog(request):
    categotias = Categoria.objects.all()
    post = POST.objects.all()

    return render(request,'Centro/Blog.html',{"post":post,"categotias":categotias})

def Blogfilt(request):
    post = POST.objects.all()

    return render(request,'Centro/Blog.html',{"post":post})



@login_required(login_url='/Login/')
def CreateBog(request):
    categotias = Categoria.objects.all()
    perfil = request.user.users
    Error=False
    Confirma=False
    if request.method=="POST":
        try:
            Ti=request.POST["Titulo"]
            Con=request.POST["Contenido"]
            Imagen = request.FILES.get('txtImagen')
            Cate = request.POST["categ"]
            POST5 = POST.objects.create(Titulo=Ti,Contenido=Con,Imagen=Imagen,Autor=perfil,Categorias=Cate)
            POST5.save()
            Confirma=True
            Error=False
        except:
            Error=True
            Confirma=False


    return render(request,"Centro/Crate_blog.html",{'Error':Error,'Confirma':Confirma,'categotias':categotias})