from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError

phone_number_validator = RegexValidator(
    regex=r'^996\d{3}\d{2}\d{2}\d{2}$',
    message="Номер телефона должен быть в формате: 996779339944"
)

class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, name, phone, password=None, **extra_fields):
        if not username:
            raise ValueError('Поле username должно быть заполнено')
        if not name:
            raise ValueError('Поле name должно быть заполнено')
        if not phone:
            raise ValueError('Поле phone должно быть заполнено')
        if not password:
            raise ValueError('Поле password должно быть заполнено')

        user = self.model(
            username=username,
            name=name,
            phone=phone,
            **extra_fields
        )

        user.set_password(password)

        try:
            user.full_clean()
        except ValidationError as e:
            raise ValueError(f"Ошибка валидации: {e}")

        user.save(using=self._db)
        return user

    def create_user(self, username, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, name, phone, password, **extra_fields)

    def create_superuser(self, username, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, name, phone, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, verbose_name='Имя')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона', validators=[phone_number_validator])
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    picture = models.ImageField(blank=True, null=True, verbose_name='Фото')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'phone']

    def __str__(self):
        return f'{self.username}'

    def get_full_name(self):
        return self.name
