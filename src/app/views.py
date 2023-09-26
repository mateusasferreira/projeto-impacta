from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from app.models import User

# Create your views here.
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

    User.objects.create_user(password=password, username=username, email=email)

    return redirect("/")