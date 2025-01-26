from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from .permissions import IsDoctorPermission
from .serializers import PatientSerializer


class PatientListView(APIView):
    permission_classes = [IsAuthenticated, IsDoctorPermission]

    def get(self, request, *args, **kwargs):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
