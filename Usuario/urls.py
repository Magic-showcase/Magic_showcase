from django.urls import path
from . import views
#importar settings para usar 2 variables
from django.conf import settings
#importar archivos static
from django.conf.urls.static import static
#django reset
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('Login/',views.Logins,name="Login"),
    path('Logout/',views.Logouts_,name="Logout"),
    path('Register/',views.Regi,name="Register"),
    path('Perfil/',views.modi,name="Perfil"),
    #Restaurar pasword
     path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='Centro/Restaurar_password/password_change.html'),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='Centro/Restaurar_password/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='Centro/Restaurar_password/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='Centro/Restaurar_password/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='Centro/Restaurar_password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Centro/Restaurar_password/password_reset_complete.html'),
         name='password_reset_complete'),
    
]