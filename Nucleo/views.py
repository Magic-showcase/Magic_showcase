from django.http import HttpResponse 
#Importar shortcuts
from django.shortcuts import render



def Home(request):
    return render(request,'Central/Home.html')

def Tutoriales(request):
    return render(request,'Central/Tutoriales.html')

def Preguntas(request):
    return render(request,'Central/Preguntas.html')

def Contactos(request):
    return render(request,'Central/Contactos.html')

    """
    Ejemplificación de manejo de información de un estilo más largo y funciones directas para el envio de variables antes de incluir una BD
    def contacto(request):
    fechahoy = datetime.datetime.now()
    equipodv = ["Yosmar Rene Rodriguez Gonzalez", "Pedro Alexander Aguilar Gonzalez","Leonel Roberto Terrazas Mejia","David Alejandro Godoy Salas "]
    maildv = ["yosmar53@gmail.com", "tem.alxaguilar@gmail.com","leoterrazas@gmai.com","alejandrogodoy723@gmail.com"]
    contacto = loader.get_template('Contacto.html')
    documento = contacto.render({"nombreuser": username, "fechahoy": fechahoy, "equipodv": equipodv, "maildv": maildv})
    return HttpResponse(documento)


   
   """
