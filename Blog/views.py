from django.shortcuts import render
from Blog.models import POST
# Create your views here.
from Blog.forms import FormularioBlog
def Blog(request):

    post = POST.objects.all()

    return render(request,'Centro/Blog.html',{"post":post})

def CreateBog(request):
    if request.method=="POST":
        Ti=request.POST["Titulo"]
        Con=request.POST["Contenido"]
        Aut=request.POST["Autor"]
        Cate=request.POST["Categorias"]



        return render(request,"Centro/gracias.html")


    return render(request,"Centro/Crate_blog.html")