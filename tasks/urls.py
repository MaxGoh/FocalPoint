from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^add/$', views.add_new_task, name='add_task'),
    url(r'^tasklist/$', views.TaskListView.as_view(), name='task_list'),
    url(r'^(?P<slug>[-\w]+)$', views.TaskDetailView.as_view(), name='task_detail'),
]
