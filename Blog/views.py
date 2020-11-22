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

def Blogfilt(request, Categoria_id):
    categotias = Categoria.objects.get(id= Categoria_id)
    cate = Categoria.objects.all()
    post = POST.objects.filter(Categorias=categotias)

    return render(request,'Centro/Categoria_Blog.html',{"post":post,"categotias":categotias,"cate":cate})



@login_required(login_url='/Login/')
def CreateBog(request):
    categotias = Categoria.objects.all()
    perfil = request.user.users
    Error=False
    Confirma=False
    if request.POST:
        posts = POST()
        posts.Autor = perfil
        posts.Titulo = request.POST.get('Titulo')
        posts.Imagen = request.FILES.get('Imagen')
        posts.Contenido = request.POST.get('Contenido')
        categoriasf = Categoria()
        categoriasf.id = request.POST.get('categ')
        posts.Categorias = categoriasf
        try:
            posts.save()
            Confirma=True
            Error=False
        except:
            Error=True
            Confirma=False


    return render(request,"Centro/Crate_blog.html",{'Error':Error,'Confirma':Confirma,'categotias':categotias})