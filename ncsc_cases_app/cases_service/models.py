from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Case(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
