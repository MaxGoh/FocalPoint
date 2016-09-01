from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Task, Note

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name','description', 'created_by']


class NoteForm(ModelForm):
    class Meta:
        model = Note
        exclude = ['task',]
        fields = ['note',]

