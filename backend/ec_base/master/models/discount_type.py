from ...common.constant.db_table import DBTable
from ...common.models.base import MasterBaseModel
from ...common.constant.app_label import ModelAppLabel


class MasterDiscountType(MasterBaseModel):
    class Meta:
        db_table = DBTable.MASTER_DISCOUNT_TYPE
        app_label = ModelAppLabel.MASTER
