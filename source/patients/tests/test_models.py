import pytest


@pytest.mark.django_db
def test_patient_model(patient):
    assert patient.diagnoses["diagnosis_1"] == "Flu"
    assert patient.date_of_birth == "1990-01-01"
