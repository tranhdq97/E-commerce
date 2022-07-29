from django.db import models

from ...common.constant.app_label import ModelAppLabel
from ...common.constant.db_table import DBTable
from ...common.models.base import DateTimeModel
from ...master.models import MasterSex, MasterCity, MasterDistrict


class UserInfo(DateTimeModel):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=20, null=True)
    dob = models.DateField(null=True)
    sex = models.ForeignKey(MasterSex, on_delete=models.RESTRICT, null=True, related_name=DBTable.USER_INFO)
    city = models.ForeignKey(MasterCity, on_delete=models.RESTRICT, null=True, related_name=DBTable.USER_INFO)
    district = models.ForeignKey(MasterDistrict, on_delete=models.RESTRICT, null=True, related_name=DBTable.USER_INFO)
    building = models.CharField(max_length=256, null=True)
    postal_code = models.CharField(max_length=6, null=True)
    phone_number = models.CharField(max_length=12, null=True)

    class Meta:
        db_table = DBTable.USER_INFO
        app_label = ModelAppLabel.USER_INFO
