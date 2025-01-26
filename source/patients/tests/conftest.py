from django.contrib.auth.models import Group
from patients.models import Patient
from accounts.models import Account
from rest_framework.test import APIClient
import pytest


@pytest.fixture
def doctor_group():
    return Group.objects.create(name='doctor')


@pytest.fixture
def doctor_user(doctor_group):
    user = Account.objects.create_user(
        username='doctor', password='password', name='Doctor Name', phone='996552365789'
    )
    user.groups.add(doctor_group)
    return user


@pytest.fixture
def admin_user():
    user = Account.objects.create_user(
        username='admin', password='password', name='Admin Name', phone='996779339966', is_staff=True
    )
    return user


@pytest.fixture
def patient():
    return Patient.objects.create(
        date_of_birth='1990-01-01',
        diagnoses={'diagnosis_1': 'Flu'},
    )


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def jwt_token(doctor_user, api_client):
    response = api_client.post('/login/', data={'username': doctor_user.username, 'password': 'password'})
    return response.data['access']
