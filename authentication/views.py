from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .forms import LoginForm


def log_in(request):
    if request.user.is_authenticated:
        return redirect("view_news")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)  # Zapisuje użytkownika w sesji.
                return redirect("view_news")
            form.add_error(None, "Nieprawidłowy login lub hasło.")
    else:
        form = LoginForm()
    return render(request, "authentication/login.html", {"form": form})


@require_POST
def log_out(request):
    logout(request)  # Usuwa dane sesji użytkownika.
    return redirect("home")
