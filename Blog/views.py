from django.shortcuts import render
from Blog.models import POST,Categoria
from Usuario.models import Users
# Create your views here.
def Blog(request):
            
    post = POST.objects.all()

    return render(request,'Centro/Blog.html',{"post":post})

def CreateBog(request):
    if request.method=="POST":
        Ti=request.POST["Titulo"]
        Con=request.POST["Contenido"]
        Cat= Categoria.objects.get(Nombre="Terror")
        Autor= Users.objects.get(user="Rene")
        POST5 = POST.objects.create(Titulo="Prueba",Contenido="adsdasdasdasd",Autor=Autor,Categorias=Cat)
        POST5.save()
        #return render(request,"Centro/gracias.html")


    return render(request,"Centro/Crate_blog.html")