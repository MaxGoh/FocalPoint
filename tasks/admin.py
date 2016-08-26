from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    fields = ('created_by', 'name', 'description',)
    list_display = ('created_at', 'created_by', 'name', 'description')
    list_filter = ('created_at', 'created_by', 'name', 'description')

admin.site.register(Task, TaskAdmin)
