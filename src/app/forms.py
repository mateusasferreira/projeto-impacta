from django import forms

from app.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Username'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label='Email'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Senha'
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username já registrado')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já registrado')
        return email
