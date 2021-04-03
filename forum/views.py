from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def dashboard(request):
    return render(request, "dashboard.html")


def contact(request):
    return render(request, "contact.html")


def signup(request):
    return render(request, "signup.html")


def login(request):
    return render(request, "login.html")


def mymemes(request):
    return render(request, "mymemes.html")


def forgot(request):
    return render(request, "forgot.html")


def notifications(request):
    return render(request, "notifications.html")


def developers(request):
    return render(request, "developers.html")


def search(request):
    return render(request, "search.html")