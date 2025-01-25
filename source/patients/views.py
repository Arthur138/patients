from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from .serializers import PatientSerializer

class PatientListView(APIView):
    permission_classes = [DjangoObjectPermissions]
    queryset = Patient.objects.none()

    def get(self, request, *args, **kwargs):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
