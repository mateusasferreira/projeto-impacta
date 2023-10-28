from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from app.forms import RegistrationForm
from app.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

# Create your views here.
@login_required
def index(request):

    users = User.objects.all()

    return render(request, "users-list.html", {'users': users})

def registration(request: HttpRequest):
    form = RegistrationForm()

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            login(request, user)

            return redirect("/")

    return render(request, 'registration/signup.html', {'form': form})


def signin(request: HttpRequest):
    if request.method == 'POST':

        login_parameter = request.POST["login"]
        password = request.POST["password"]

        user = authenticate(request, user=login_parameter, password=password)

        if user is not None:
            login(request, user)

            return redirect("/")

        return render(request, "registration/login.html", {'error': 'Usuário e/ou senha incorretos'})

    return render(request, "registration/login.html")
