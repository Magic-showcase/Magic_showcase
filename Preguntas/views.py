from django.shortcuts import render
#importar core.mail
from django.core.mail import send_mail
#importar settings
from django.conf import settings

def Preguntas(request):
    Error=False
    Confirma=False
    if request.method=="POST":
        try:
            sujeto=request.POST["asunto"]
        
            mensaje=request.POST["mensaje"]+" "+ request.POST["email"]
        
            email_from = settings.EMAIL_HOST_USER
        
            recipient_list = ["Magic.showcase.questions@gmail.com"]
        
            send_mail(sujeto,mensaje,email_from,recipient_list)
            Confirma=True
            Error=False
        except:
            Error=True
            Confirma=False
    
    return render(request,'Centro/Preguntas.html',{'Error':Error,'Confirma':Confirma})