from django.db import models

from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_table import DBTable
from ec_base.common.constant.master import MasterCustomerTypeID
from ec_base.common.models.base import CustomBaseUserModel
from ec_base.master.models import MasterCustomerType
from ec_base.user_info.models import UserInfo


class Customer(CustomBaseUserModel):
    is_leave = models.BooleanField(default=False)
    info = models.OneToOneField(UserInfo, on_delete=models.RESTRICT, null=True, related_name=DBTable.CUSTOMER)
    type = models.ForeignKey(MasterCustomerType, on_delete=models.RESTRICT, related_name=DBTable.CUSTOMER)

    @property
    def is_staff(self):
        return False

    def save(self, *args, **kwargs):
        self.type_id = MasterCustomerTypeID.UNVERIFIED
        super(Customer, self).save(*args, **kwargs)

    class Meta:
        db_table = DBTable.CUSTOMER
        app_label = ModelAppLabel.CUSTOMER
