#Importar libreria serial 
import serial,time

from django.http import HttpResponse 
#Importar shortcuts
from django.shortcuts import render
from Usuario.models import Users
from django.contrib.auth.decorators import login_required
from .models import Item,Showcase

@login_required(login_url='/Login/')
def Itemcre(request):
    perfil = request.user.users
    Error=False
    Confirma=False
    if request.POST:
        Ite = Item()
        Ite.Usuario = perfil
        Ite.Nombre = request.POST.get('Nombre')
        Ite.Seccion = request.POST.get('Seccion')
        Ite.Contenido = request.POST.get('Contenido')
        Ite.Precio = request.POST.get('Precio')
        Ite.Imagen = request.FILES.get('Imagen')
        try:
            Ite.save()
            Confirma=True
            Error=False
        except:
            Error=True
            Confirma=False


    return render(request,"Centro/Itemcreate.html",{'Error':Error,'Confirma':Confirma})

@login_required(login_url='/Login/')
def Vicre(request):
    perfil = request.user.users
    Ite = Item.objects.filter(Usuario=perfil)
    Error=False
    Confirma=False
    if request.POST:
        Sho = Showcase()
        Sho.Usuario = perfil
        Sho.Nombrevi = request.POST.get('Nombre')
        Sho.Seccion = request.POST.get('Seccion')

        Slot1 = Item()
        Slot2 = Item()
        Slot3 = Item()
        Slot4 = Item()
        Slot5 = Item()
        Slot6 = Item()
        Slot7 = Item()
        Slot8 = Item()
        Slot9 = Item()

        Slot1.id = request.POST.get('Item1')
        Slot2.id = request.POST.get('Item2')
        Slot3.id = request.POST.get('Item3')
        Slot4.id = request.POST.get('Item4')
        Slot5.id = request.POST.get('Item5')
        Slot6.id = request.POST.get('Item6')
        Slot7.id = request.POST.get('Item7')
        Slot8.id = request.POST.get('Item8')
        Slot9.id = request.POST.get('Item9')

        Sho.Slot1 = Slot1
        Sho.Slot2 = Slot2
        Sho.Slot3 = Slot3
        Sho.Slot4 = Slot4
        Sho.Slot5 = Slot5
        Sho.Slot6 = Slot6
        Sho.Slot7 = Slot7
        Sho.Slot8 = Slot8
        Sho.Slot9 = Slot9
        try:
            Sho.save()
            Confirma=True
            Error=False
        except:
            Error=True
            Confirma=False


    return render(request,"Centro/Crearvit.html",{'Error':Error,'Confirma':Confirma,'Ite':Ite})

@login_required(login_url='/Login/')
def Servicio_Control(request):
    perfil = request.user.users
    Items = Item.objects.filter(Usuario=perfil)
    Show = Showcase.objects.filter(Usuario=perfil)
    serial_error = False
    posi = 5
    if request.method == 'POST':
        datos_to_encode = request.POST.get('Led')
        posi = datos_to_encode
        try:
            serial_connection = serial.Serial('/dev/ttyUSB0', 9600)
            time.sleep(2)
            serial_connection.write(datos_to_encode.encode())
            serial_connection.close()
            serial_error = False
        except serial.SerialException:
              serial_error = True
    return render(request,'Centro/Servicio_Control.html', {'serial_error': serial_error,"perfil":perfil,"Items":Items,"Show":Show,"posi":posi})