from rest_framework import generics

from work.models import Machine
from work.serializers import MachineSerializer


class MachineList(generics.ListAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = ()