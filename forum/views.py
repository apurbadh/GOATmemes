from django.shortcuts import render
from .models import Users, Memes
from django.shortcuts import redirect


# Create your views here.
def index(request):
    if request.session.get("logged"):
        return redirect('/dashboard')
    return render(request, "index.html")


def dashboard(request):
    if not request.session.get("logged"):
        return redirect("/")
    users = Users.objects.all()[:3]
    email = request.session.get("email")
    user = Users.objects.filter(email=email).first()
    meme = Memes.objects.all()
    content = {"user": user, "memes": meme, "top": users}
    return render(request, "dashboard.html", content)


def contact(request):
    return render(request, "contact.html")


def signup(request):
    if request.session.get("logged"):
        return redirect('/dashboard')
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
    if request.session.get("logged"):
        return redirect('/dashboard')
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
    if not request.session.get("logged"):
        return redirect("/")
    email = request.session.get("email")
    user = Users.objects.filter(email=email).first()
    users = Users.objects.all()[:3]
    meme = Memes.objects.filter(posted_by_email=email)
    content = {"user": user, "memes": meme, "top": users}
    return render(request, "mymemes.html", content)


def forgot(request):
    return render(request, "forgot.html")


# def notifications(request):
#     if not request.session.get("logged"):
#         return redirect("/")
#     email = request.session.get("email")
#     user = Users.objects.filter(email=email).first()
#     content = {"user": user}
#     return render(request, "notifications.html", content)


def developers(request):
    return render(request, "developers.html")


def search(request):
    if not request.session.get("logged"):
        return redirect("/")
    query = request.GET["query"]
    email = request.session.get("email")
    memes = Memes.objects.filter(caption__contains=query)
    user = Users.objects.filter(email=email).first()
    users = Users.objects.all()[:3]
    content = {"user": user, "memes": memes, "query": query, "top": users}
    return render(request, "search.html", content)


def post(request):
    if request.method == "POST":
        caption = request.POST.get("caption")
        image = request.FILES.get("img")
        user = Users.objects.filter(email=request.session.get("email")).first()
        user.number_of_memes += 1
        user.save()
        meme = Memes(posted_by=user.name, posted_by_email=user.email, caption=caption, likes=0, usr_img=user.pic, meme=image)
        meme.save()
    return redirect("/")


def logout(request):
    request.session["logged"] = False
    return redirect("/")