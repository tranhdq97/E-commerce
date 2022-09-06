from django.db import models
from django.db.models import ForeignKey

from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_fields import MasterDistrictFields
from ec_base.common.constant.db_table import DBTable
from ec_base.common.constant.related_name import RelatedName
from ec_base.common.models.base import BaseMasterModel
from ec_base.master.models.city import MasterCity


class MasterDistrict(BaseMasterModel):
    city = ForeignKey(MasterCity, related_name=RelatedName.MASTER_DISTRICT, on_delete=models.RESTRICT)
    name = models.CharField(max_length=255, unique=False)

    class Meta:
        db_table = DBTable.MASTER_DISTRICT
        app_label = ModelAppLabel.MASTER
        unique_together = [MasterDistrictFields.NAME, MasterDistrictFields.CITY]
