
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from .models import Users

def Logins(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('Home')
        else:
            return render(request,'Centro/Login.html',{'error':'Usuario y/o contraseña erronea'})
    
    return render(request,'Centro/Login.html' )
