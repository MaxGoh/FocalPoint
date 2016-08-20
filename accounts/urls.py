from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'login/$', views.login_view, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'logout/$', views.logout_view, name='logout'),
    url(r'register/$', views.register_new, name='register'),
]