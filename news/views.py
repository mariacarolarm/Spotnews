from django.shortcuts import render, redirect
from news.models import CategoryForm, News


def index(request):
    context = {"news_list": News.objects.all()}
    return render(request, 'home.html', context)


def news(request, id):
    context = {"news_details": News.objects.get(id=id)}
    return render(request, 'news_details.html', context)


def new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = CategoryForm()
        context = {'form': form}
        return render(request, 'categories_form.html', context)
