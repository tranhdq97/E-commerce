from django.db import models
from django.db.models import ForeignKey

from .city import MasterCity
from ...common.constant.db_table import DBTable
from ...common.constant.related_name import RelatedName
from ...common.models.base import MasterBaseModel
from ...common.constant.app_label import ModelAppLabel


class MasterDistrict(MasterBaseModel):
    city = ForeignKey(MasterCity, related_name=RelatedName.MASTER_DISTRICT, on_delete=models.RESTRICT)

    class Meta:
        db_table = DBTable.MASTER_DISTRICT
        app_label = ModelAppLabel.MASTER
