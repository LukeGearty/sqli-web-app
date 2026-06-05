from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="SQL Injection Vulnerability"),
    path("login/", views.login, name="Login"),
    path("search/", views.search_users, name="Search")
]