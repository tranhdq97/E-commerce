from django.contrib.auth.base_user import BaseUserManager
from django.core.management.base import CommandError


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have an email address.')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        if self.filter(is_admin=True).exists():
            raise CommandError("There is no room for two.")

        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
