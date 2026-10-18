"""Lokalne konto i przykładowe dane bez duplikatów."""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangolab.settings")

import django
django.setup()

from django.contrib.auth import get_user_model
from django.utils import timezone
from news.models import News
from tasks.models import Task

user, created = get_user_model().objects.get_or_create(username="student")
if created:
    user.set_password("Student123!")
    user.save()
    print("Utworzono konto: student / Student123!")
else:
    print("Konto student juz istnieje - haslo pozostaje bez zmian.")

News.objects.get_or_create(
    topic="Pierwsza wiadomość",
    defaults={
        "text": "Ta wiadomość jest zapisana w bazie SQLite.",
        "author": "student",
        "create_time": timezone.now(),
        "last_edit_time": timezone.now(),
    },
)
Task.objects.get_or_create(title="Przygotować pokaz Django")
print("Dane demonstracyjne sa gotowe.")
