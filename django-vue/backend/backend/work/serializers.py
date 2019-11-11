from rest_framework import serializers
from work.models import (Case, Machine, Problem)

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = (
            '__all__')


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = (
            'id', 'name')

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = (
            'id', 'name')
