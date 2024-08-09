from django.shortcuts import render, redirect
from administra.models import Mascota
from django.core.paginator import Paginator


def base(request):
    return render(request, 'base.html')


def mas(request):
    masc = Mascota.objects.all()
    paginator = Paginator(masc, 5)
    pagina = request.GET.get("page") or 1
    lista = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, lista.paginator.num_pages + 1)
    return render(request, 'mascotas_registradas.html', {'mascotas': lista, 'paginas': paginas, 'pagina_actual': pagina_actual})


