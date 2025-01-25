from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Patient
from .serializers import PatientSerializer
from .permissions import IsDoctorPermission


class PatientListView(APIView):
    permission_classes = [IsDoctorPermission]

    def get(self, request, *args, **kwargs):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
