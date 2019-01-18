from django.contrib import admin
from .models import Project, Task


class TaskInLine(admin.TabularInline):
    model = Task
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['project_name']}),
    ]
    def total_tasks(self, obj):
        return obj.task_set.count()

    def completed_tasks(self, obj):
        return obj.task_set.filter(is_complete=True).count()

    # project_task_count.short_description = "Total tasks"
    inlines = [TaskInLine]
    list_display = ('project_name', 'is_complete', 'total_tasks', 'completed_tasks')
    list_filter = ['is_complete']
    search_fields = ['project_name']

admin.site.register(Project, ProjectAdmin)

admin.site.site_header = 'ML|Edge Administration'
