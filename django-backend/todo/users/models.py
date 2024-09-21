from django.contrib.auth.models import AbstractUser
from django.db import models

from categories.models import Category


class CustomUser(AbstractUser):
    telegram_user_id = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
