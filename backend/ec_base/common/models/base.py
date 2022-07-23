from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models import ForeignKey

from .managers import CustomUserManager
from ..utils.middleware import get_current_user


class CurrentUserField(ForeignKey):
    def __init__(self, to, provider, **kwargs):
        self.provider = provider
        self.auto_current = kwargs.pop('auto_current', False)
        self.auto_current_add = kwargs.pop('auto_curren_add', False)
        super().__init__(to, **kwargs)

    def pre_save(self, model_instance, add):
        if self.auto_current or (self.auto_current_add and add):
            current_user = get_current_user()

            if current_user and current_user.is_authenticated and current_user.provider == self.provider:
                user_id = current_user.id
                setattr(model_instance, self.attname, user_id)
                return user_id

        return super().pre_save(model_instance, add)


class StaffCreator(models.Model):
    creator_staff = CurrentUserField(
        to='staff.Staff',
        provider='staff',
        auto_curren_add=True,
        null=True,
        on_delete=models.RESTRICT,
        related_name="%(app_label)s_%(class)s_creator_staff"
    )

    class Meta:
        abstract = True


class StaffEditor(models.Model):
    editor_staff = CurrentUserField(
        to='staff.Staff',
        provider='staff',
        auto_curren_add=True,
        null=True,
        on_delete=models.RESTRICT,
        related_name="%(app_label)s_%(class)s_editor_staff"
    )

    class Meta:
        abstract = True


class DateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class CustomBaseUserModel(AbstractBaseUser, DateTimeModel):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    class Meta:
        abstract = True


class BaseMasterModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
