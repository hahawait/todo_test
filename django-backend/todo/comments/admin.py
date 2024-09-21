from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'user', 'content', 'created_at', 'updated_at')
    list_filter = ('task', 'user', 'created_at', 'updated_at')
    search_fields = ('content', 'user', 'task')


admin.site.register(Comment, CommentAdmin)
