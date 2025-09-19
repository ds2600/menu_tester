from django.urls import path
from . import views

app_name = "menu_tester"

urlpatterns = [
    path("github/", views.github_redirect, name="github"),
]
