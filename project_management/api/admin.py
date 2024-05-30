from django.contrib import admin
from .models import Client, Project

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'created_at', 'created_by')
    search_fields = ('client_name', 'created_by__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'client', 'created_at', 'created_by')
    search_fields = ('project_name', 'client__client_name', 'created_by__username')
    list_filter = ('created_at', 'client')
    ordering = ('-created_at',)
    filter_horizontal = ('users',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
