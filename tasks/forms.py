from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory

from .models import Task, Note, Duration

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name','description']


class NoteForm(ModelForm):
    class Meta:
        model = Note
        exclude = ['task',]
        fields = ['name', 'note', 'url']

class DurationForm(ModelForm):
    total_second = forms.IntegerField(required=True);

    class Meta:
        model = Duration
        fields =  ['total_second']
