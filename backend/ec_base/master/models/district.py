from django.db import models
from django.db.models import ForeignKey

from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_fields import MasterDistrictFields, MasterFields
from ec_base.common.constant.db_table import DBTable
from ec_base.common.models.base import MasterBaseModel
from ec_base.master.models.city import MasterCity


class MasterDistrict(MasterBaseModel):
    city = ForeignKey(MasterCity, on_delete=models.RESTRICT, related_name=DBTable.MASTER_DISTRICT)
    name = models.CharField(max_length=255, unique=False)

    class Meta:
        db_table = DBTable.MASTER_DISTRICT
        app_label = ModelAppLabel.MASTER
        unique_together = [MasterFields.NAME, MasterDistrictFields.CITY]
