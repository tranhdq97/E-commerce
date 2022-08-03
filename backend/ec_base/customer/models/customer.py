from django.db import models

from ...common.constant.app_label import ModelAppLabel
from ...common.constant.db_table import DBTable
from ...common.models.base import Creator, Editor
from ...user_info.models import UserInfo


class Customer(Creator, Editor):
    info = models.OneToOneField(UserInfo, on_delete=models.RESTRICT, null=True, related_name=DBTable.CUSTOMER)

    class Meta:
        db_table = DBTable.CUSTOMER
        app_label = ModelAppLabel.CUSTOMER

    @property
    def is_staff(self):
        return False
