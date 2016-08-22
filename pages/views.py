from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'pages/home.html', {'navbar': 'home'})

def about_view(request):
    return render(request, 'pages/about.html', {'navbar': 'about'})

def contact_view(request):
    return render(request, 'pages/contact.html', {'navbar': 'contact'})

@login_required(login_url="/login/")
def profile_view(request):
    return render(request, 'pages/profile.html')

@login_required(login_url="/login/")
def dashboard_view(request):
    return render(request, 'pages/dashboard.html')
