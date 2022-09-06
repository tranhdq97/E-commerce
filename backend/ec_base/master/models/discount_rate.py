from django.db import models

from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_table import DBTable
from ec_base.common.models.base import BaseMasterModel


class MasterDiscountRate(BaseMasterModel):
    name = models.IntegerField(unique=True)

    class Meta:
        db_table = DBTable.MASTER_DISCOUNT_RATE
        app_label = ModelAppLabel.MASTER
