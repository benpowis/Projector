import datetime
from django.utils import timezone
from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.project_name

    def total_tasks(self):
        return self.task_set.count()

    def completed_tasks(self):
        return self.task_set.filter(is_complete=True).count()

    def completed_perc(self):
        total = self.task_set.count()
        complete = self.task_set.filter(is_complete=True).count()
        def safe_div(x,y):
            if y == 0:
                return 0
            return x / y
        perc = safe_div(complete,total)
        return round(perc, 2)*100

    def proj_is_complete(self):
        total = self.task_set.count()
        complete = self.task_set.filter(is_complete=True).count()
        if complete == total:
            pass
            Project.objects.filter(pk=self.pk).update(is_complete='True')
            return True
        Project.objects.filter(pk=self.pk).update(is_complete='False')
        return False

    def complete_icon(self):
        total = self.task_set.count()
        complete = self.task_set.filter(is_complete=True).count()
        if complete == total:
            pass
            return '<i class="material-icons blue-text">check_box</i>'
        return '<i class="material-icons blue-text">check_box_outline_blank</i>'

    def total_projects(self):
        return project_name.count()

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    task_desc = models.TextField(max_length=600)
    due_date = models.DateField('due date')
    is_complete = models.BooleanField(default=False)

    task_desc.short_description = "Task description"
    def __str__(self):
        return self.task_name

    def icon(self):
        if self.is_complete==True:
            return '<i class="material-icons blue-text ">check_box</i>'
        else:
            return '<i class="material-icons blue-text ">check_box_outline_blank</i>'

    def past_due(self):
        if self.due_date < datetime.date.today():
            return True
        else:
            return False
