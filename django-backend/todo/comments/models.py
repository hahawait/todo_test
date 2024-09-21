from django.db import models
from users.models import CustomUser

from models import TimeStampMixin
from utils import generate_custom_pk

from tasks.models import Task


class Comment(TimeStampMixin):
    id = models.CharField(max_length=64, primary_key=True, default=generate_custom_pk, editable=False)
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'Comment by {self.user} on {self.task}'
