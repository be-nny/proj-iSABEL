from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("sign-up", views.signUp, name="signUp"),
    path("map", views.userMap, name="userMap"),
    path("leaderboard", views.leaderboard, name="leaderboard"),
    path("about", views.about, name="about"),
    path("profile", views.profile, name="profile"),
]