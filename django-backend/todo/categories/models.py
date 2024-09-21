from django.db import models

from models import TimeStampMixin
from utils import generate_custom_pk


class Category(TimeStampMixin):
    id = models.CharField(max_length=64, primary_key=True, default=generate_custom_pk, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
