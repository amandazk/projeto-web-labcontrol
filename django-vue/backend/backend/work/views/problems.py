from rest_framework import generics

from work.models import Problem
from work.serializers import ProblemSerializer


class ProblemList(generics.ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = ()