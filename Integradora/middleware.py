
from django.shortcuts import redirect
from django.urls import reverse


class veriperfil:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

#        if not request.user.is_anonymous:
#            users = request.user.users
#            if not users.Photo or not users.bio:
#                if request.path not in [reverse('Perfil'),reverse('Logout')]:
#                    return redirect('Perfil')
        # Code to be executed for each request/response after
        # the view is called.
        response = self.get_response(request)
        return response