from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create test users (superadmin) for local development'

    def handle(self, *args, **options):
        from users.models import User

        username = 'superadmin'
        password = 'Superadmin123!'
        email = 'admin@example.com'
        role = 'SUPERADMIN'

        user, created = User.objects.get_or_create(username=username, defaults={
            'email': email,
            'role': role,
            'is_staff': True,
            'is_superuser': True,
            'is_active': True,
        })

        if not created:
            self.stdout.write(self.style.NOTICE(f'User "{username}" already exists — updating password and role.'))
            user.role = role
            user.email = email
            user.is_staff = True
            user.is_superuser = True

        user.set_password(password)
        user.save()

        self.stdout.write(self.style.SUCCESS(f'User "{username}" ready. Password: {password}'))
