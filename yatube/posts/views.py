# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse(f'Групповые сообщения {slug}')
