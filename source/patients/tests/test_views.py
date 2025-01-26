import pytest


@pytest.mark.django_db
def test_patient_list_view_for_doctor(api_client, doctor_user, patient, jwt_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token)
    response = api_client.get('/patients/')
    assert response.status_code == 200
    assert len(response.data) > 0
    assert response.data[0]['diagnoses'] == {"diagnosis_1": "Flu"}
