from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.forms import PasswordInput

from .models import MyUser


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = MyUser
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            return user


class MyUserLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=PasswordInput())


class MyUserChangePasswordForm(forms.Form):
    password1 = forms.CharField(widget=PasswordInput())
    password2 = forms.CharField(widget=PasswordInput())
