from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'pages/home.html')

@login_required(login_url="/login/")
def profile_view(request):
    return render(request, 'pages/profile.html')
