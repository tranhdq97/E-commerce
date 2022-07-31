from rest_framework import serializers

from ..models.district import MasterDistrict
from ...common.constant.db_fields import MasterDistrictFields, CommonFields


class MasterDistrictSlz(serializers.ModelSerializer):
    class Meta:
        model = MasterDistrict
        fields = (CommonFields.ID, MasterDistrictFields.NAME, MasterDistrictFields.CITY)
