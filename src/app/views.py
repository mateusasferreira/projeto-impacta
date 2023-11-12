from django.views.generic import ListView, DetailView
from django import forms
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from app.forms import LoginForm, RegistrationForm
from app.models import User, Message
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

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

class LoginView(FormView):
    template_name = "registration/login.html"
    form_class = LoginForm

    def form_valid(self, form: forms.Form):
        login_parameter = form.cleaned_data["login"]
        password = form.cleaned_data["password"]

        user = authenticate(self.request, user=login_parameter, password=password)

        if user is not None:
            login(self.request, user)
            redirect_url = self.request.POST.get('next', '')

            if len(redirect_url) == 0:
                redirect_url = "/"
            
            
            return redirect(redirect_url)
        
        messages.error(self.request, "Usuário e/ou senha inválidos")

        return super().form_invalid(form=form)


class UsersList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users-list.html'
    

class UserDetails(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user-details.html'  # Create this template in your templates folder
    context_object_name = 'user'  # This is the variable name available in the template
    pk_url_kwarg = 'id' 


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
        


