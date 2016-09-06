from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as django_login
from django.dispatch import Signal

from .forms import UserCreateForm

def login_view(request, *args, **kwargs):
    response = django_login(request, *args, **kwargs)
    if isinstance(response, HttpResponseRedirect):
        messages.success(request, 'You have successfully logged in.')
    return response


def register_new(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Your account has been created.')
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'accounts/register.html', {'form': form, 'navbar': 'register'})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return HttpResponseRedirect('/')
