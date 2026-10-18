from django.db import models


class Task(models.Model):
    title = models.CharField("Nazwa zadania", max_length=120)

    def __str__(self):
        return self.title
