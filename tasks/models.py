from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

import datetime

class TaskManager(models.Manager):
    def create_task(self, name, creator):
        new_task = self.model(name=name, created_by=creator)
        new_task.save()
        return new_task


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    created_by = models.ForeignKey(User)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name

    def save(self):
        if not self.id:
            self.created = datetime.datetime.today()
        self.updated = datetime.datetime.today()
        super(Task, self).save()

    objects = TaskManager()


