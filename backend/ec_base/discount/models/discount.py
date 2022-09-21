from django.db import models

from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_table import DBTable
from ec_base.common.models.base import Creator, Editor, DateTimeModel
from ec_base.master.models import MasterDiscountType, MasterDiscountRate


class Discount(DateTimeModel, Creator, Editor):
    is_deleted = models.BooleanField(default=False)
    discount_type = models.ForeignKey(
        to=MasterDiscountType,
        on_delete=models.RESTRICT,
        related_name=DBTable.DISCOUNT,
    )
    discount_rate = models.ForeignKey(
        to=MasterDiscountRate,
        on_delete=models.RESTRICT,
        related_name=DBTable.DISCOUNT,
    )

    class Meta:
        db_table = DBTable.DISCOUNT
        app_label = ModelAppLabel.DISCOUNT
