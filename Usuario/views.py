
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from .models import Users


from Usuario.forms import Perilmodi

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

    perfil = request.user.users

    if request.method == 'POST':
        form = Perilmodi(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Users.Photo = data['Photo']
            #Users.country = data['country']
            #Users.bio = data['bio']
            Users.save()
            messages.success(request,'perfil actualizado!')
            return redirect('Blog')
        
    else:
        form = Perilmodi()

    return render(request=request,template_name='Centro/Perfil.html',context={'Users':Users,'user':request.user,'form':form})