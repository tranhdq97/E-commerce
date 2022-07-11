from ...common.constant.db_table import DBTable
from ...common.models.base import MasterBaseModel
from ...common.constant.app_label import ModelAppLabel


class MasterProductCategory(MasterBaseModel):
    class Meta:
        db_table = DBTable.MASTER_PRODUCT_CATEGORY
        app_label = ModelAppLabel.MASTER
