from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.utils import timezone


from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@login_required
def add_new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user # Get Current User
            obj.save()
            return redirect('/tasks/test/')
    else:
        form = TaskForm()
    return render(request, "tasks/add.html", {'form': form})

def task_detail_view(request, slug):
    task = get_object_or_404(Task, slug=slug)
    return render(request, 'tasks/detail.html', {
        'task': task,
    })
