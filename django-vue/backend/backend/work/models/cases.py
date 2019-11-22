from django.db import models
from django.db.models.fields import DateTimeField

class Case(models.Model):
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
        return str((self.problem,self.machine))
    
    @property
    def problemname(self):
        return str(self.problem.problem)

    @property
    def machinename(self):
        return str(self.machine.name)
    
