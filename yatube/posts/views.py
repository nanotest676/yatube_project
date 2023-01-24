# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template)


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse(f'Групповые сообщения {slug}')
