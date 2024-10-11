from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='sev2316@yandex.ru',
            first_name='Admin',
            last_name='Adminov',
            country='Russia',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('1234')
        user.save()