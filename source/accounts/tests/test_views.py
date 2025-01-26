import pytest
from rest_framework import status
from django.contrib.auth import get_user_model


@pytest.fixture
def user():
    return get_user_model().objects.create_user(
        username='testuser',
        name='Test User',
        phone='996779339944',
        password='password123'
    )


@pytest.mark.django_db
def test_login_success(client, user):
    response = client.post('/login/', data={'username': 'testuser', 'password': 'password123'})
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data


@pytest.mark.django_db
def test_login_invalid_credentials(client, user):
    response = client.post('/login/', data={'username': 'testuser', 'password': 'wrongpassword'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_login_missing_credentials(client):
    response = client.post('/login/', data={})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
