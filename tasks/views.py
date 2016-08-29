from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils import timezone


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
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, "tasks/add.html", {'form': form})


class TaskListView(generic.ListView):
    template_name = "tasks/task_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


def task_detail_view(request, slug):
    task = get_object_or_404(Task, slug=slug)
    return render(request, 'tasks/detail.html', {'task': task})


class TaskDetailView(generic.DetailView):
    model = Task
    template_name="tasks/detail.html"
