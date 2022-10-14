from django.db import models

from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_table import DBTable
from ec_base.common.models.base import Creator, Editor, DateTimeModel
from ec_base.file_management.models import FileManagement
from ec_base.master.models import MasterProductCategory


class Product(Creator, Editor, DateTimeModel):
    name = models.CharField(max_length=256)
    quantity = models.IntegerField(default=0)
    purchase_price = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    desc = models.TextField()
    is_deleted = models.BooleanField(default=False)
    category = models.ForeignKey(to=MasterProductCategory, on_delete=models.RESTRICT, related_name=DBTable.PRODUCT)
    photo = models.ForeignKey(to=FileManagement, on_delete=models.RESTRICT, related_name=DBTable.PRODUCT, null=True)

    class Meta:
        unique_together = (('name', 'category'),)
        db_table = DBTable.PRODUCT
        app_label = ModelAppLabel.PRODUCT
