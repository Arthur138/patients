from accounts.models import Account
import pytest


@pytest.mark.django_db
def test_doctor_access(api_client, doctor_user, patient, jwt_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token)
    response = api_client.get('/patients/')
    assert response.status_code == 200
    assert len(response.data) > 0


@pytest.mark.django_db
def test_admin_access(api_client, admin_user, patient, jwt_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token)
    response = api_client.get('/patients/')
    assert response.status_code == 200
    assert len(response.data) > 0


@pytest.mark.django_db
def test_non_doctor_access(api_client, patient, jwt_token):
    user = Account.objects.create_user(username='user', password='password', name='User', phone='996778996655')
    response = api_client.post('/login/', data={'username': user.username, 'password': 'password'})
    new_user_token = response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + new_user_token)
    response = api_client.get('/patients/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthenticated_access(api_client, patient):
    response = api_client.get('/patients/')
    assert response.status_code == 401
