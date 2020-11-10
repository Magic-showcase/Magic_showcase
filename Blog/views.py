from django.shortcuts import render
from Blog.models import POST,Categoria
# Create your views here.
from django.contrib.auth.models import User
def Blog(request):

    post = POST.objects.all()

    return render(request,'Centro/Blog.html',{"post":post})

def CreateBog(request):
    if request.method=="POST":
        Ti=request.POST["Titulo"]
        Con=request.POST["Contenido"]
        Cat= Categoria.objects.get(Nombre="Terror")
        Autor= User.objects.get(first_name="Rene")
        POST5 = POST.objects.create(Titulo="Prueba",Contenido="adsdasdasdasd",Autor=Autor,Categorias=Cat)
        POST5.save()
        #return render(request,"Centro/gracias.html")


    return render(request,"Centro/Crate_blog.html")