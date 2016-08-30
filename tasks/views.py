from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages

from .models import Task
from .forms import TaskForm

@login_required
def add_new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user # Get Current User
            obj.save()
            messages.success(request, 'Task has been successfully created')
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, "tasks/add.html", {'form': form})


def task_for_user(user):
    return Task.objects.filter(created_by=user)

def delete_selected_task(request, slug):
    selected_task = get_object_or_404(Task, slug=slug)
    selected_task.delete()
    messages.success(request, 'Task has been successfully deleted')
    return redirect('dashboard')

class TaskListView(generic.ListView):
    template_name = "includes/task_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        #return Task.objects.filter(created_by=self.request.user)
        return task_for_user(self.request.user)


class TaskDetailView(generic.DetailView):
    model = Task
    template_name="tasks/detail.html"
