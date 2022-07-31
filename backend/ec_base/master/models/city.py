from ...common.constant.app_label import ModelAppLabel
from ...common.constant.db_table import DBTable
from ...common.models.base import BaseMasterModel


class MasterCity(BaseMasterModel):
    class Meta:
        db_table = DBTable.MASTER_CITY
        app_label = ModelAppLabel.MASTER
