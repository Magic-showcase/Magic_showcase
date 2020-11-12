
from django.contrib.auth import authenticate, login , logout
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

@login_required
def Logouts_(request):
    logout(request)
    return redirect('Home')

def Regi(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  
        password_confirmacion = request.POST['Passwd_confir']
        
        if password != password_confirmacion:
            return render(request, 'Centro/Singup.html',{'error':'Las contraseñas no coinciden '})
        try:
            usernu = User.objects.create_user(username=username,password=password)
        except IntegrityError:
            return render(request, 'Centro/Singup.html',{'error':'Usuario en existencia '})

        usernu.first_name = request.POST['Nombre']
        usernu.last_name = request.POST['Apellido']
        usernu.email = request.POST['Email']
        usernu.save()

        return redirect('Login')

    return render(request,'Centro/Singup.html')

@login_required
def modi(request):

    return render(request,'Centro/Perfil.html')