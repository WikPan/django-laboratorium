from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("", include("authentication.urls")),
    path("news/", include("news.urls")),
    path("tasks/", include("tasks.urls")),
]
