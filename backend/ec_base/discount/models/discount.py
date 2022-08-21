from django.db import models

from ...common.constant.app_label import ModelAppLabel
from ...common.constant.db_table import DBTable
from ...common.models.base import Creator, Editor, DateTimeModel
from ...master.models import MasterDiscountType, MasterDiscountRate


class Discount(DateTimeModel, Creator, Editor):
    is_deleted = models.BooleanField(default=False)
    discount_type = models.ForeignKey(to=MasterDiscountType, on_delete=models.RESTRICT, related_name=DBTable.DISCOUNT, )
    discount_rate = models.ForeignKey(to=MasterDiscountRate, on_delete=models.RESTRICT, related_name=DBTable.DISCOUNT, )

    class Meta:
        db_table = DBTable.DISCOUNT
        app_label = ModelAppLabel.DISCOUNT
