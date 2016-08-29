import itertools

from django.forms import ModelForm
from django import forms
from django.utils.text import slugify
from .models import Task

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['name','description', 'slug']
