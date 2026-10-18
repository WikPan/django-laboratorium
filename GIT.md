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
git show release:main.txt
```

`main.txt` jest małym plikiem do ćwiczenia gałęzi. Kod Django jest na każdej taki sam.
Plik `pierwszy.cpp` to przykład z instrukcji Gita, nie część aplikacji Django.

## .gitignore

W `.gitignore` są pliki pomijane przez Git: środowisko `.venv`, baza SQLite,
pliki tymczasowe, archiwa i PDF-y. Reguła `*.cpp` pokazuje przykład z instrukcji:

```powershell
git ls-files pierwszy.cpp
git check-ignore drugi.cpp
```

Pierwszy plik został zapisany przed dodaniem reguły i nadal jest śledzony.
Drugi, dodany później, jest ignorowany. Możesz utworzyć kolejny `.cpp`, żeby to pokazać.

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

## GitHub - do wykonania po utworzeniu repozytorium

Lokalna historia jest gotowa. Nie została wysłana na GitHub.

1. Zaloguj się na https://github.com i wybierz **New repository**.
2. Nazwij je np. `django-laboratorium`. Wybierz widoczność według potrzeb.
3. Zostaw puste opcje tworzenia README, .gitignore i licencji, po czym utwórz repozytorium.
4. Skopiuj jego adres HTTPS i wstaw w poleceniu zamiast `ADRES_REPOZYTORIUM`:

```powershell
git remote add origin ADRES_REPOZYTORIUM
git push -u origin master
git push -u origin develop
git push -u origin feature_1
git push -u origin feature_2
git push -u origin feature_3
git push -u origin release
git push origin --tags
```

GitHub może poprosić o zalogowanie w przeglądarce.
Późniejsze zmiany na aktualnej gałęzi wysyłasz przez `git push`.
`git fetch` pobiera informacje i obiekty ze zdalnego repozytorium bez zmiany plików roboczych.
`git pull` pobiera zmiany i włącza je do aktualnej gałęzi.

Żeby pokazać klonowanie, otwórz terminal w innym folderze i wykonaj:

```powershell
git clone ADRES_REPOZYTORIUM Django-kopia
```

Do sprawozdania zrób zrzut historii, gałęzi, taga i repozytorium na GitHubie.
Dodaj też zrzuty samodzielnie wykonywanych etapów, w tym rozwiązywania konfliktu.
Samo lokalne repozytorium nie kończy części zadania dotyczącej GitHuba.
