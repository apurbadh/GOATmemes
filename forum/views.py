from django.shortcuts import render
from .models import Users
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request, "index.html")


def dashboard(request):
    if not request.session.get("logged"):
        return redirect("/")
    email = request.session.get("email")
    user = Users.objects.filter(email=email).first()
    content = {"user": user}
    return render(request, "dashboard.html", content)


def contact(request):
    return render(request, "contact.html")


def signup(request):
    content = {'mes' : ""}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        date = request.POST.get("date")
        address = request.POST.get("address")
        country = request.POST.get("country")
        img = request.FILES.get("img")
        if Users.objects.filter(email=email):
            content["mes"] = "User with that email already exists"
        else:
            user = Users(name=name, email=email, password=password, birthdate=date, city=address, country=country, pic=img)
            user.save()
            content["mes"] = "Successfully Registered"

    return render(request, "signup.html", content)


def login(request):
    content = {"mes" : ""}
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = Users.objects.filter(email=email).first()
        if not user:
            content["mes"] = "User doesn't exist"
        elif user.password != password:
            content["mes"] = "Password does not match"
        else:
            request.session["logged"] = True
            request.session["email"] = email
            return redirect("/dashboard")
    return render(request, "login.html", content)


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