from django.utils import timezone
from .models import Perfil

def user_online_status(request):
    context = {}
    if request.user.is_authenticated:
        now = timezone.now()
        status_threshold = now - timezone.timedelta(minutes=5)
        perfil, created = Perfil.objects.get_or_create(user=request.user)
        perfil.online = perfil.user.last_login and perfil.user.last_login > status_threshold
        perfil.save()
        context['user_is_online'] = perfil.online
    else:
        context['user_is_online'] = False
    return context
