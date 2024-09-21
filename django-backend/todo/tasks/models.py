from django.db import models
from users.models import CustomUser

from models import TimeStampMixin
from utils import generate_custom_pk

from categories.models import Category


class Task(TimeStampMixin):
    id = models.CharField(max_length=64, primary_key=True, default=generate_custom_pk, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    category = models.ManyToManyField(Category, related_name='tasks')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'due_date']),
        ]

    def __str__(self):
        return self.title
