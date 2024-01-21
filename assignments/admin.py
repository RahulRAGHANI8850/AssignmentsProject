from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(assignment)
class ShowAssignments(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'msg', 'time', 'projectFile']

