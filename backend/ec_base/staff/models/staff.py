from django.contrib import admin
from django.db import models

from ...common.constant.app_label import ModelAppLabel
from ...common.constant.db_table import DBTable
from ...common.constant.master import MasterStaffID
from ...common.models.base import CustomBaseUserModel
from ...master.models import MasterStaffType
from ...user_info.models.user_info import UserInfo


class Staff(CustomBaseUserModel):
    is_leave = models.BooleanField(default=False)
    info = models.OneToOneField(to=UserInfo, on_delete=models.RESTRICT, null=True, related_name=DBTable.STAFF)
    type = models.ForeignKey(MasterStaffType, on_delete=models.RESTRICT, default=MasterStaffID.UNAPPROVED,
                             related_name=DBTable.STAFF)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return True

    @property
    def is_super_staff(self):
        return self.is_admin

    def save(self, *args, **kwargs):
        if self.is_admin:
            self.type_id = MasterStaffID.SUPER_STAFF

        super(Staff, self).save(*args, **kwargs)

    class Meta:
        db_table = DBTable.STAFF
        app_label = ModelAppLabel.STAFF


admin.site.register(Staff)
