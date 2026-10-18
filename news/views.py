from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import NewsForm
from .models import News


def index(request):
    news = News.objects.order_by("-create_time", "-id")
    return render(request, "news/index.html", {"news": news})


def detail(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, "news/view.html", {"news": news})


@login_required
def add(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user.username
            news.create_time = timezone.now()
            news.last_edit_time = news.create_time
            news.save()
            return redirect("view_news")
    else:
        form = NewsForm()
    return render(request, "news/add.html", {"form": form, "title": "Dodaj wiadomość"})


@login_required
def edit(request, id):
    news = get_object_or_404(News, id=id)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.last_edit_time = timezone.now()
            news.save()
            return redirect("news_detail", id=news.id)
    else:
        form = NewsForm(instance=news)
    return render(request, "news/add.html", {"form": form, "title": "Edytuj wiadomość"})
