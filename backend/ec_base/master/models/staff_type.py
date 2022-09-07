from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_table import DBTable
from ec_base.common.models.base import MasterBaseModel


class MasterStaffType(MasterBaseModel):
    class Meta:
        db_table = DBTable.MASTER_STAFF_TYPE
        app_label = ModelAppLabel.MASTER
