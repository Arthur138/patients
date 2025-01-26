import pytest
from patients.serializers import PatientSerializer


@pytest.mark.django_db
def test_patient_serializer(patient):
    serializer = PatientSerializer(patient)
    assert serializer.data['date_of_birth'] == '1990-01-01'
    assert serializer.data['diagnoses'] == {'diagnosis_1': 'Flu'}
