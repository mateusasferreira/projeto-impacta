from django.views.generic import ListView, DetailView, CreateView
from django import forms
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
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


class UserDetails(DetailView):
    template_name = "user-details.html"
    pk_url_kwarg = "id"
    queryset = User.objects.prefetch_related('messages_received').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        return context


class UserMessageCreateView(CreateView):
    model = Message
    fields = ['message']

    def form_valid(self, form):
        form.instance.receiver_id = self.kwargs['id']
        form.instance.sender = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        success_url = reverse('user-details', args=[self.kwargs['id']])
        return success_url

@login_required
def delete_message(request: HttpRequest, id):
    if (request.method == 'POST'):
        message = get_object_or_404(Message, id=id)
        
        if request.user == message.sender or request.user == message.receiver:
            message.delete()

        next_url = request.GET.get('next', '')
        return redirect(next_url)
        


