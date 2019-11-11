from django.db import models
from django.db.models.fields import DateTimeField


class Problem(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name