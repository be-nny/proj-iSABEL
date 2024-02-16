from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

# Create your views here.
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def scan(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return render(request, "site/scan.html", {})

def userNotLoggedIn(request):
    logout(request)
    return render(request, "registration/login-signup.html", {})

def loginSignup(request):
    return render(request, "registration/login-signup.html", {})

def userMap(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return HttpResponse("Map page")

def leaderboard(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return HttpResponse("Leaderboard page")

def profile(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return HttpResponse("Profile page")

def about(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return HttpResponse("About page")