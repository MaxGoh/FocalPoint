from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as django_login

from django.conf import settings
from .forms import loginForm

def login_view(request, *args, **kwargs):
    response = django_login(request, *args, **kwargs)
    if isinstance(response, HttpResponseRedirect):
        messages.success(request, 'You have successfully logged in.')
    return response


def register_new(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Your account has been created.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return HttpResponseRedirect('/home/')


