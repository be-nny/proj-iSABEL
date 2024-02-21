from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

"""
Initialises the login and sign up flow
"""
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

"""
View for the scan page, if a user isn't logged in, they are redirected
"""
def scan(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return render(request, "site/scan.html", {})
"""
When a user isn't logged in, they are redirected to the log in and sign up page
"""
def userNotLoggedIn(request):
    logout(request)
    return render(request, "registration/login-signup.html", {})

"""
View for the login and sign up page
"""
def loginSignup(request):
    return render(request, "registration/login-signup.html", {})

"""
View for the user map page, if a user isn't logged in, they are redirected
"""
def userMap(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return render(request, "site/map.html", {})

"""
View for the leaderboard page, if a user isn't logged in, they are redirected
"""
def leaderboard(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return HttpResponse("Leaderboard page")

"""
View for the users profile page, if a user isn't logged in, they are redirected
"""
def profile(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return HttpResponse("Profile page")

"""
View for the about page, if a user isn't logged in, they are redirected
"""
def about(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return HttpResponse("About page")
