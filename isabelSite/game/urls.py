from django.urls import path
from . import views
from .views import SignUp

urlpatterns = [
    path("sign-up", SignUp.as_view(), name="signUp"),
    path("logout", views.userNotLoggedIn, name="logout_view"),
    path("login-signup", views.loginSignup, name="login-signup"),
    path("scan", views.scan, name="scan"),
    path("rewards", views.rewards, name="rewards"),
    path("leaderboard", views.leaderboard, name="leaderboard"),
    path("about", views.about, name="about"),
    path("profile", views.profile, name="profile"),
]