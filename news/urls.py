from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="view_news"),
    path("add/", views.add, name="news_add"),
    path("<int:id>/", views.detail, name="news_detail"),
    path("<int:id>/edit/", views.edit, name="news_edit"),
]
