from rest_framework import serializers
from work.models import (Case, Machine, Problem)

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ('id','problem','machine','problemname','machinename')


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = (
            '__all__')

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = (
            '__all__')
