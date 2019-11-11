from django.db import models
from django.db.models.fields import DateTimeField

class Case(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField() #descrição detalhada caso necessário
    problem = models.ForeignKey(
        'Problem',
        related_name="cases",
        on_delete=models.CASCADE,
        null=True
    )
    machine = models.ForeignKey(
        'Machine',
        related_name="cases",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name
