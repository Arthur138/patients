from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from patients.models import Patient


class Command(BaseCommand):
    help = 'Создание группы doctor и добавление прав модели Patient'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='doctor')

        if created:
            self.stdout.write(self.style.SUCCESS('Группа doctor успешно создана!'))
        else:
            self.stdout.write(self.style.SUCCESS('Группа doctor уже существует!'))

        content_type = ContentType.objects.get_for_model(Patient)
        permissions = Permission.objects.filter(content_type=content_type)
        group.permissions.add(*permissions)

        self.stdout.write(self.style.SUCCESS('Все права для модели Patient успешно добавлены группе doctor!'))
