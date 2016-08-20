from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'logout/$', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'register/$', views.register_new, name='register'),
]