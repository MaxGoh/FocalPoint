from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.conf import settings
from .forms import UserCreationForm

def login_view(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page
    else:
        # Invalid
        # Return an 'invalid login' error message.
        return HttpResponse("Invalid Login")

def logout_view(request):
    logout(request)
    # Redirect to login page
    return render(request, settings.LOGIN_URL)

def register_new(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
