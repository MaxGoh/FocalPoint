from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import FormView

from .models import Task, Note, Duration
from .forms import TaskForm, NoteForm, DurationForm

@login_required
def add_new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user # Get Current User
            obj.save()
            messages.success(request, 'Task has been successfully created')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, "tasks/add.html", {'form': form})


def task_for_user(user):
    return Task.objects.filter(created_by=user)


def delete_selected_task(request, slug):
    selected_task = get_object_or_404(Task, slug=slug)
    selected_task.delete()
    messages.success(request, 'Task has been successfully deleted')
    return redirect('task_list')


def delete_selected_note(request, pk, slug):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    selected_task = get_object_or_404(Task, slug=slug)
    messages.success(request, 'Note has been deleted')
#    return redirect('task_list')
    return HttpResponseRedirect(reverse('task_detail', kwargs={'slug':selected_task.slug}))


class TaskListView(generic.ListView):
    template_name = "tasks/task_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        #return Task.objects.filter(created_by=self.request.user)
        return task_for_user(self.request.user)

class TaskDetailView(FormMixin, generic.DetailView):
    model = Task
    template_name="tasks/detail.html"
    form_class = NoteForm
    form_class2 = DurationForm
    form_classes = {
        'noteform': NoteForm,
        'durationform': DurationForm,
    }

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['note_form'] = self.get_form()
        context['notes'] = Note.objects.filter(task__slug=self.kwargs['slug'])
        context['duration'] = Duration.objects.all()

        return context

    def get_success_url(self):
        return reverse('task_detail', kwargs={'slug': self.kwargs['slug']})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        current_task = get_object_or_404(Task, slug=self.kwargs['slug'])
        self.object = form.save(commit=False)
        self.object.task =  current_task
        self.object.save()
        return HttpResponse(self.get_success_url())


