from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Task
from .forms import TaskForm

def add_new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user # Get Current User
            task.save()
            return redirect('/tasks/test/')
    else:
        form = TaskForm()
    return render(request, "tasks/add.html", {'form': form})

class TaskListView(ListView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context