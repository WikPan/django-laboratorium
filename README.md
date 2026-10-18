# Prosty pokaz Django

## Uruchomienie

Kliknij **URUCHOM.cmd**, otwórz **http://127.0.0.1:8000/**.
Login: **student**, hasło: **Student123!**.
Potrzebny Python 3.10+; przy pierwszym uruchomieniu Internet.

## Co pokazać prowadzącemu

1. Otwórz wiadomości bez logowania.
2. Kliknij Zadania - pojawi się logowanie.
3. Zaloguj się i zmień treść jednej wiadomości.
4. W Zadaniach dodaj zadanie, zmień jego nazwę i usuń je.
5. Wyloguj się i pokaż, że Zadania znów wymagają logowania.

## Co powiedzieć i gdzie to pokazać w kodzie

| Co mówię | Gdzie pokazuję |
| --- | --- |
| „Tutaj adres jest przypisany do funkcji.” | `tasks/urls.py`: `path(...)` |
| „Tutaj jest tabela z nazwą zadania. ID dodaje Django.” | `tasks/models.py`: klasa `Task` |
| „Tutaj formularz korzysta z pola tego modelu.” | `tasks/forms.py`: klasa `TaskForm` |
| „Tutaj pobieram zadania z bazy.” | `tasks/views.py`: funkcja `index`, `Task.objects.order_by(...)` |
| „Tutaj zapisuję nowe zadanie.” | `tasks/views.py`: funkcja `add`, `form.save()` |
| „Tutaj zmieniam istniejące zadanie.” | `tasks/views.py`: funkcja `edit`, `instance=task` |
| „Tutaj usuwam zadanie.” | `tasks/views.py`: funkcja `delete`, `task.delete()` |
| „To wymaga zalogowania.” | `tasks/views.py`: `@login_required` nad funkcjami |
| „Tutaj sprawdzam login i hasło, loguję i wylogowuję.” | `authentication/views.py`: `authenticate`, `login`, `logout` |
| „Tutaj wyświetlam dane w HTML.” | `templates/tasks/index.html`: pętla `for` i `{{ task.title }}` |
| „Dane są w pliku SQLite.” | `djangolab/settings.py`: `DATABASES`; plik `db.sqlite3` |

Całość: **adres -> funkcja w Pythonie -> baza danych -> strona HTML**.
GET pokazuje stronę lub formularz, POST przesyła dane do zapisania.
`form.is_valid()` sprawdza dane, a `form.save()` zapisuje je w bazie.
`{% csrf_token %}` jest tokenem ochronnym formularza POST wymaganym przez Django.

Wiadomości są przykładem z materiałów, a Zadania własną aplikacją z jednym polem.
Wylogowanie i edycja wiadomości realizują pozostałe punkty zadania.

## Git

Ten projekt ma też repozytorium Git. Krótki pokaz i polecenia są w **GIT.md**.
