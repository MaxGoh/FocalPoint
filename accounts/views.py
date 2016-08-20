from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

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

