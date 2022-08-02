from django.db import models

from ...common.constant.app_label import ModelAppLabel
from ...common.constant.db_table import DBTable
from ...common.models.base import BaseMasterModel


class MasterDiscountRate(BaseMasterModel):
    name = models.IntegerField(unique=True)

    class Meta:
        db_table = DBTable.MASTER_DISCOUNT_RATE
        app_label = ModelAppLabel.MASTER
