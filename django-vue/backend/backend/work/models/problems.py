from django.db import models
from django.db.models.fields import DateTimeField


class Problem(models.Model):
    problem = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.problem