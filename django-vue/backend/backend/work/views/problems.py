from rest_framework import generics, permissions


from work.models import Problem
from work.serializers import ProblemSerializer


class ProblemList(generics.ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = ()

class ProblemCreate(generics.CreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )