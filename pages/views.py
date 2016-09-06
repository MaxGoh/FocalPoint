from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from tasks import views as task_view

def home_view(request):
    """
    Return /
    """
    return render(request, 'pages/home.html', {'navbar': 'home'})


def about_view(request):
    """
    Return /about/
    """
    return render(request, 'pages/about.html', {'navbar': 'about'})


def contact_view(request):
    """
    Return /contact/
    """
    return render(request, 'pages/contact.html', {'navbar': 'contact'})


def faq_view(request):
    return render(request, 'pages/faq.html', {'navbar': 'faq'})


@login_required(login_url="/login/")
def profile_view(request):
    return render(request, 'pages/profile.html')


@login_required(login_url="/login/")
def dashboard_view(request):
    tasks = task_view.task_for_user(request.user)
    return render(request, 'pages/dashboard.html', {'tasks': tasks})
