from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="tasks"),
    path("add/", views.add, name="task_add"),
    path("<int:id>/edit/", views.edit, name="task_edit"),
    path("<int:id>/delete/", views.delete, name="task_delete"),
]
