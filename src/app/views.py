from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from app.forms import RegistrationForm
from app.models import User, Message
from django.contrib.auth import authenticate, login

# Create your views here.

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


@login_required
def index(request):

    users = User.objects.all()

    return render(request, "users-list.html", {'users': users})

@login_required
def user_details(request, id):
    user = User.objects.select_related().get(id=id)

    user.messages = user.messages_received.all()

    return render(request, "user-details.html", {'user': user})


@login_required
def user_message(request: HttpRequest, id):
    if(request.method == 'POST'):
        
        Message.objects.create(
            receiver_id=id,
            sender_id=request.user.id,
            message=request.POST.get('message')
        )

    return redirect(f"/users/{id}")