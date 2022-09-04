from crum import get_current_user
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models import ForeignKey

from ec_base.common.models.managers import CustomUserManager


class CurrentUserField(ForeignKey):
    def __init__(self, to, **kwargs):
        self.auto_current = kwargs.pop('auto_current', False)
        self.auto_current_add = kwargs.pop('auto_current_add', False)
        super().__init__(to, **kwargs)

    def pre_save(self, model_instance, add):
        if self.auto_current or (self.auto_current_add and add):
            current_user = get_current_user()

            if current_user and current_user.is_authenticated:
                user_id = current_user.id
                setattr(model_instance, self.attname, user_id)
                return user_id

        return super().pre_save(model_instance, add)


class Creator(models.Model):
    created_by = CurrentUserField(
        to='staff.Staff',
        auto_current_add=True,
        null=True,
        on_delete=models.RESTRICT,
        related_name="%(app_label)s_%(class)s_created_by"
    )

    class Meta:
        abstract = True


class Editor(models.Model):
    updated_by = CurrentUserField(
        to='staff.Staff',
        auto_current=True,
        null=True,
        on_delete=models.RESTRICT,
        related_name="%(app_label)s_%(class)s_updated_by"
    )

    class Meta:
        abstract = True


class CustomerCreator(models.Model):
    created_by = CurrentUserField(
        to='customer.Customer',
        auto_current_add=True,
        null=True,
        on_delete=models.RESTRICT,
        related_name="%(app_label)s_%(class)s_created_by"
    )

    class Meta:
        abstract = True


class CustomerEditor(models.Model):
    updated_by = CurrentUserField(
        to='customer.Customer',
        auto_current=True,
        null=True,
        on_delete=models.RESTRICT,
        related_name="%(app_label)s_%(class)s_updated_by"
    )

    class Meta:
        abstract = True


class DateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class CustomBaseUserModel(AbstractBaseUser, DateTimeModel):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return False

    def __str__(self):
        return f"{self.email}"

    class Meta:
        abstract = True


class BaseMasterModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
