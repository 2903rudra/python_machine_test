from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_clients', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.client_name
    
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_projects', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.project_name
