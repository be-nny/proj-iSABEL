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
    path('resolve', views.resolve, name='resolve'),
    path("users", views.users, name="users"),
    path("update_user_from_bcode", views.update_user_from_bcode, name="update_user_from_bcode"),
    path("checkout", views.checkout, name="checkout"),
    path("buy_voucher", views.buy_voucher, name="buy_voucher"),
    path("reset_password", views.resetPassword, name="reset_password"),
    path("reset_password_code", views.resetPasswordCode, name="reset_password_code"),
    path("exp_demo", views.expDemo, name="exp_demo")


]