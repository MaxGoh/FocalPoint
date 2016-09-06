from django.contrib import admin
from .models import Task, Note

class TaskAdmin(admin.ModelAdmin):
    fields = ('created_by', 'name', 'description', 'slug')
    list_display = ('id', 'pk', 'created_at', 'created_by', 'name', 'slug', 'description',)
    list_filter = ('created_at', 'created_by', 'name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

    def add_view(self, request, form_url="", extra_context=None):
        """
        Automatically select the current user in the 'created_by' field
        """
        data = request.GET.copy()
        data['created_by'] = request.user
        request.GET = data
        return super(TaskAdmin, self).add_view(request, form_url="", extra_context=extra_context)

    def get_readonly_fields(self, request, obj=None):
        """
        Prevents 'created_by' to be edited after initial creation
        """
        if obj is not None:
            return self.readonly_fields + ('created_by',)
        return self.readonly_fields



class NoteAdmin(admin.ModelAdmin):
    fields = ('name', 'note',)
    list_display = ('id', 'pk', 'created_at', 'name', 'note',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Note, NoteAdmin)
