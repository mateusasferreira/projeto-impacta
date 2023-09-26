from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from app.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q

# Create your views here.
@login_required
def index(request):
    return HttpResponse('Hello World')

def registration(request):
    return render(request, 'registration/signup.html')

def create_user(request: HttpRequest):
    if len(request.POST.keys()) == 0:
        return redirect("/registration")

    password =  request.POST["password"]
    email = request.POST["email"]
    username = request.POST["username"]

    user_already_registered = User.objects.filter(Q(email=email) | Q(username=username)).first()

    if user_already_registered is not None:
        return render(request, "registration/signup.html", {'error': 'Username ou email já registrados'})

    user = User.objects.create_user(password=password, username=username, email=email)
    login(request, user)


    return redirect("/")