from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserCreateForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    #first_name = forms.CharField(required=True)
    #last_name = forms.CharField(required=True)

    class Meta:
        model = User
#        fields = ("username", "email", "password1", "password2", "first_name", "last_name")
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
#        user.first_name = self.cleaned_data["first_name"]
#        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'span2','placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'span2','placeholder':'Password'}))
