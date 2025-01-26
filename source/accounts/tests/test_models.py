import pytest
from accounts.models import Account


@pytest.mark.django_db
def test_create_user():
    user = Account.objects.create_user(
        username='testuser',
        name='Test User',
        phone='996779336944',
        password='password123'
    )
    assert user.username == 'testuser'
    assert user.name == 'Test User'
    assert user.phone == '996779336944'
    assert user.check_password('password123')
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_superuser():
    superuser = Account.objects.create_superuser(
        username='admin',
        name='Admin User',
        phone='996779339945',
        password='adminpassword'
    )
    assert superuser.username == 'admin'
    assert superuser.is_staff
    assert superuser.is_superuser


@pytest.mark.django_db
def test_create_user_without_required_fields():
    with pytest.raises(ValueError):
        Account.objects.create_user(username='', name='No Username', phone='996779339946', password='password123')

    with pytest.raises(ValueError):
        Account.objects.create_user(username='testuser', name='', phone='996779339946', password='password123')

    with pytest.raises(ValueError):
        Account.objects.create_user(username='testuser', name='Test User', phone='', password='password123')


@pytest.mark.django_db
def test_invalid_phone_number():
    with pytest.raises(ValueError) as excinfo:
        Account.objects.create_user(username='user1', name='User One', phone='999779339944', password='password123')

    assert "Номер телефона должен быть в формате: 996779339944" in str(excinfo.value)
