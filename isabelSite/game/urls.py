from django.urls import path
from . import views
from .views import SignUp

urlpatterns = [
    path("sign-up", SignUp.as_view(), name="signUp"),
    path("logout", views.userNotLoggedIn, name="logout_view"),
    path("login-signup", views.loginSignup, name="login-signup"),
    path("scan", views.scan, name="scan"),
    path("rewards", views.rewards, name="rewards"),
    path("expDemo", views.expDemo, name="expDemo"),
    path("leaderboard", views.leaderboard, name="leaderboard"),
    path("about", views.about, name="about"),
    path("profile", views.profile, name="profile"),
    path("reports", views.reports, name="reports"),
    path("users", views.users, name="users"),
    path("update_user_from_bcode", views.update_user_from_bcode, name="update_user_from_bcode"),
    path("buy_voucher", views.buy_voucher, name="buy_voucher"),
    path("save-report", views.save_report, name='save_report'),


]