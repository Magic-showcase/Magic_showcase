#Importar libreria serial 
import serial,time

from django.http import HttpResponse 
#Importar shortcuts
from django.shortcuts import render
from Usuario.models import Users
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/Login/')
def Servicio_Control(request):
    perfil = request.user.users
    serial_error = False
    if request.method == 'POST':
        datos_to_encode = request.POST.get('Led')
        try:
            serial_connection = serial.Serial('/dev/ttyUSB0', 9600)
            time.sleep(2)
            serial_connection.write(datos_to_encode.encode())
            serial_connection.close()
            serial_error = False
        except serial.SerialException:
              serial_error = True
    return render(request,'Centro/Servicio_Control.html', {'serial_error': serial_error,"perfil":perfil})