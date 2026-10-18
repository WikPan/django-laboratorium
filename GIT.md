# Prosty pokaz Gita na projekcie Django

Git zapisuje kolejne wersje plików. Nie zmienia sposobu uruchamiania Django.

## Co powiedzieć i pokazać

Otwórz terminal w folderze projektu:

```powershell
git status
git log --oneline --graph --all --decorate
git branch
git tag -n
```

- „Commit to zapisana wersja projektu. Tutaj widać historię.”
- „Gałąź pozwala robić zmiany osobno. Mam master, develop i trzy feature.”
- „Merge łączy zmiany. Dwie gałęzie zmieniły to samo miejsce w main.txt,
  więc przy łączeniu wybrałem wynik zawierający obie zmiany.”
- „Release to przygotowana wersja, a tag v1.0.0.0 oznacza konkretny commit.”

Zmiany między gałęziami pokaż tak:

```powershell
git show feature_1:main.txt
git show feature_2:main.txt
git show v1.0.0.0:main.txt
```

`main.txt` był małym plikiem do ćwiczenia gałęzi. Przykłady zostały usunięte
z bieżącego folderu, ale są w historii. Pokazujesz je poleceniem `git show`.
Kod Django jest na każdej gałęzi taki sam.

## .gitignore

W `.gitignore` są pliki pomijane przez Git: środowisko `.venv`, baza SQLite,
pliki tymczasowe, archiwa i PDF-y. Reguła `*.cpp` pokazuje przykład z instrukcji:

```powershell
git show v1.0.0.0:pierwszy.cpp
git check-ignore przyklad.cpp
```

Pierwsze polecenie pokazuje plik zapisany przed dodaniem reguły.
Drugie pokazuje, że nowy plik `.cpp` będzie ignorowany. Nie musisz go tworzyć.

## Zapisanie kolejnej zmiany

Zmień jakiś tekst w `README.md`, a następnie:

```powershell
git diff
git add README.md
git commit -m "Zmiana opisu projektu"
git status
```

`diff` pokazuje różnice, `add` wybiera zmiany do zapisu, `commit` zapisuje wersję.
Przygotowane są też skróty `git st` (status) i `git hist` (historia).
Jeśli chcesz okno z historią, użyj `gitk --all`.

## GitHub

Repozytorium: https://github.com/WikPan/django-laboratorium

Wysłane są gałęzie master, develop, feature_1, feature_2, feature_3 i release
oraz tag v1.0.0.0. Adres `origin` jest już ustawiony. Możesz go sprawdzić:

```powershell
git remote -v
```

Jeżeli `origin` istnieje i ma błędny adres, zmieniasz go przez `set-url`:

```powershell
git remote set-url origin https://github.com/WikPan/django-laboratorium.git
```

Późniejsze zmiany na aktualnej gałęzi wysyłasz przez `git push`.
`git fetch` pobiera informacje i obiekty ze zdalnego repozytorium bez zmiany plików roboczych.
`git pull` pobiera zmiany i włącza je do aktualnej gałęzi.

Żeby pokazać klonowanie, otwórz terminal w innym folderze i wykonaj:

```powershell
git clone https://github.com/WikPan/django-laboratorium.git Django-kopia
```

Do sprawozdania zrób zrzut historii, gałęzi, taga i repozytorium na GitHubie.
Dodaj też zrzuty samodzielnie wykonywanych etapów, w tym rozwiązywania konfliktu.
