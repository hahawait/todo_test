from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'due_date', 'user', 'completed')
    list_filter = ('category', 'user', 'completed')
    search_fields = ('title', 'description')
    date_hierarchy = 'due_date'
    filter_horizontal = ('category',)
