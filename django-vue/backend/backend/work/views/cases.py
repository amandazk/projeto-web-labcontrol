from rest_framework import generics, permissions

from work.models import Case
from work.serializers import CaseSerializer


class CaseList(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = ()


class CaseDestroy(generics.DestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class CaseUpdate(generics.UpdateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class CaseCreate(generics.CreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )


class CaseGet(generics.RetrieveAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = ()
