from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Task


@login_required
def index(request):
    # Pobieramy zadania z bazy i przekazujemy je do HTML.
    tasks = Task.objects.order_by("id")
    return render(request, "tasks/index.html", {"tasks": tasks})


@login_required
def add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Zapis nowego zadania w bazie.
            return redirect("tasks")
    else:
        form = TaskForm()  # GET: pokazujemy pusty formularz.
    return render(request, "tasks/form.html", {"form": form, "title": "Dodaj zadanie"})


@login_required
def edit(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # instance=task oznacza edycję tego zadania.
            return redirect("tasks")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/form.html", {"form": form, "title": "Edytuj zadanie"})


@login_required
def delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()  # Usuwamy po kliknięciu przycisku potwierdzenia.
        return redirect("tasks")
    return render(request, "tasks/delete.html", {"task": task})
