from django.shortcuts import render
from news.models import News


def index(request):
    context = {"news_list": News.objects.all()}
    return render(request, 'home.html', context)


def news(request, id):
    context = {"news_details": News.objects.get(id=id)}
    return render(request, 'news_details.html', context)
