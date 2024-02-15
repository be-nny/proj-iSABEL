from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index page")

def login(request):
    return HttpResponse("Login page")

def signUp(request):
    return HttpResponse("Sign up page")

def scan(request):
    return HttpResponse("Scan page")

def userMap(request):
    return HttpResponse("Map page")

def leaderboard(request):
    return HttpResponse("Leaderboard page")

def profile(request):
    return HttpResponse("Profile page")

def about(request):
    return HttpResponse("About page")