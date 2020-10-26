from django.shortcuts import render
from Blog.models import POST
# Create your views here.

def Blog(request):

    post = POST.objects.all()

    return render(request,'Centro/Blog.html',{"post":post})
