from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^add/$', views.add_new_task, name='add_task'),
    url(r'^test/$', views.TaskListView.as_view(), name='task_list')
]
