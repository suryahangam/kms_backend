from django.db import models
from user.models import TimestampedModel
from kms.utils import generate_unique_ID
from django.utils import timezone


class Project(TimestampedModel):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('abandoned', 'Abandoned'),
        ('on_hold', 'On Hold'),
    ]
    project_id = models.CharField(max_length=50, default=generate_unique_ID(), 
                                  unique=True)
    project_title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    project_type = models.CharField(max_length=50) # make it choice field
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, 
                              default='not_started')
    
    def start_project(self):
        self.start_date = timezone.now().date()
        return self.start_date
    
    def set_deadline(self):
        if self.start_date:
            self.end_date = timezone.now().date()
            return True
        return False


class ProjectGroup(TimestampedModel):
    group_name = models.CharField(max_length=250)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('user.CustomUser', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.group_name


class Email(TimestampedModel):
    pass


class Contribution(TimestampedModel):
    description = models.CharField(max_length=255, null=True, blank=True)
    contribution_date = models.DateField(default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    contributor = models.ForeignKey('user.CustomUser', on_delete=models.SET_NULL, null=True)
    contribution_point = models.FloatField()

    def __str__(self):
        if self.description:
            return self.description
        return self.project.title
    
    def get_user_contribution(self, user):
        pass

    def get_user_points(self, user):
        pass

    def get_project_contributions(self, project):
        pass
    
