from ...common.constant.app_label import ModelAppLabel
from ...common.constant.db_table import DBTable
from ...common.models.base import BaseMasterModel


class MasterShippingStatus(BaseMasterModel):
    class Meta:
        db_table = DBTable.MASTER_SHIPPING_STATUS
        app_label = ModelAppLabel.MASTER
