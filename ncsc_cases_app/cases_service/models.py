import datetime

from django.db import models
from django.utils import timezone


class Case(models.Model):
    # case_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
