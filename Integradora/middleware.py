
from django.shortcuts import redirect
from django.urls import reverse


class veriperfil:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.users
                if not profile.Photo or not profile.bio:
                    if request.path not in [reverse('Perfil'), reverse('logout')]:
                        return redirect('Perfil')

        response = self.get_response(request)
        return response