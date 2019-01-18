from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.core.paginator import Paginator

from .models import Project, Task


class IndexView(generic.ListView):
    queryset = Project.objects.order_by('is_complete')[:10]
    template_name = 'projects/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        """Return 10 projects."""
        return Project.objects.order_by('is_complete')[:10]

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["total_projects"] = Project.objects.count()
        data["total_tasks"] = Task.objects.count()
        data["total_due_tasks"] = Task.objects.filter(is_complete=False).count()
        return data


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

class InsightView(generic.TemplateView):
    template_name = 'projects/insight.html'
