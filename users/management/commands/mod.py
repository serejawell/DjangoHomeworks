from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Create moderator user and group with permissions'

    def handle(self, *args, **options):
        # Получаем кастомную модель пользователя
        User = get_user_model()

        # Создание группы модераторов
        moderator_group, created = Group.objects.get_or_create(name='Moderators')

        # Правила для добавления в группу
        permissions = [
            'can_edit_description',
            'can_edit_category',
            'set_published',
        ]

        for perm in permissions:
            try:
                permission = Permission.objects.get(codename=perm)
                moderator_group.permissions.add(permission)
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Permission {perm} does not exist.'))

        # Создание пользователя
        user = User.objects.create(
            email='moder@yandex.ru',
            first_name='Moder',
            last_name='Moderov',
            is_superuser=False,  # Измени на False, если не нужен суперпользователь
            is_staff=True,  # Убедись, что модератор может входить в админку
        )

        user.set_password('1234')
        user.save()

        # Добавление пользователя в группу модераторов
        moderator_group.user_set.add(user)

        self.stdout.write(self.style.SUCCESS(f'Successfully created user {user.first_name} {user.last_name} and added to Moderators group.'))
