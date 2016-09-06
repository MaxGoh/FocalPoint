from django import forms
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)


class UserCreateForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    date_of_birth = forms.DateField(input_formats=["%d %B, %Y"], widget=forms.widgets.DateInput(format="%d %B, %Y"))


    class Meta:
        model = User
        fields = ("username", "email", "date_of_birth", "password1", "password2", "first_name", "last_name")
#        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.date_of_birth = self.cleaned_data["date_of_birth"]
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'span2','placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'span2','placeholder':'Password'}))
