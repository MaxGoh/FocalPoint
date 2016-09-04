from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^add$', views.add_new_task, name='add_task'),
    url(r'^list$', views.TaskListView.as_view(), name='task_list'),
    url(r'^(?P<slug>[-\w]+)$', views.TaskDetailView.as_view(), name='task_detail'),
    url(r'^(?P<slug>[-\w]+)/delete_task$', views.delete_selected_task, name='task_delete'),
    url(r'^(?P<slug>[-\w]+)/(?P<pk>\d+)/delete_note$', views.delete_selected_note, name='note_delete'),
]
