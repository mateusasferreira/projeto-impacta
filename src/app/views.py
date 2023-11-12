from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from app.forms import RegistrationForm
from app.models import User, Message
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
# Create your views here.

class RegistrationView(FormView):
    template_name = "registration/signup.html"
    form_class = RegistrationForm
    success_url = "/"

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )

        login(self.request, user)
        
        return super().form_valid(form)


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

    return render(request, "user-details.html", {'user': user, 'logged_user': request.user})


@login_required
def user_message(request: HttpRequest, id):
    if(request.method == 'POST'):
        
        Message.objects.create(
            receiver_id=id,
            sender_id=request.user.id,
            message=request.POST.get('message')
        )

    return redirect(f"/users/{id}")

@login_required
def delete_message(request: HttpRequest, id):
    if (request.method == 'POST'):
        message = get_object_or_404(Message, id=id)
        
        if request.user == message.sender or request.user == message.receiver:
            message.delete()

        next_url = request.GET.get('next', '')
        return redirect(next_url)
        


