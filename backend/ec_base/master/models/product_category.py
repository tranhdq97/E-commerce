from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_table import DBTable
from ec_base.common.models.base import MasterBaseModel


class MasterProductCategory(MasterBaseModel):
    class Meta:
        db_table = DBTable.MASTER_PRODUCT_CATEGORY
        app_label = ModelAppLabel.MASTER
