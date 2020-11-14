from django.shortcuts import render
from Blog.models import POST,Categoria
from Usuario.models import Users
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
def Blog(request):
     
    post = POST.objects.all()

    return render(request,'Centro/Blog.html',{"post":post})

@login_required(login_url='/Login/')
def CreateBog(request):
    if request.method=="POST":
        Ti=request.POST["Titulo"]
        Con=request.POST["Contenido"]
        #Cat = Categoria.objects.get(id=1)
        #Cate = get_object_or_404(Categoria, id=4)
        Cate = Categoria.objects.filter(id='1')
        Autor= Users.objects.get(user_id=1)
        POST5 = POST.objects.create(Titulo="Prueba",Contenido="adsdasdasdasd",Autor=Autor,Categorias=Cate)
        POST5.save()
        #return render(request,"Centro/gracias.html")


    return render(request,"Centro/Crate_blog.html")