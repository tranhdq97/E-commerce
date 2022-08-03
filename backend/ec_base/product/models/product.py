from django.db import models

from ...common.constant.app_label import ModelAppLabel
from ...common.constant.db_table import DBTable
from ...common.models.base import Creator, Editor, DateTimeModel
from ...file_management.models import FileManagement
from ...master.models import MasterProductCategory


class Product(Creator, Editor, DateTimeModel):
    name = models.CharField(max_length=256)
    quantity = models.IntegerField(default=0)
    purchase_price = models.FloatField(default=0.)
    price = models.FloatField(default=0.)
    desc = models.TextField()
    is_deleted = models.BooleanField(default=False)
    category = models.ForeignKey(to=MasterProductCategory, on_delete=models.RESTRICT, related_name=DBTable.PRODUCT)
    photo = models.ForeignKey(to=FileManagement, on_delete=models.RESTRICT, related_name=DBTable.PRODUCT, null=True)

    class Meta:
        db_table = DBTable.PRODUCT
        app_label = ModelAppLabel.PRODUCT
