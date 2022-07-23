from rest_framework import serializers

from ..models.district import MasterDistrict
from ...common.constant.db_fields import MasterDistrictFields


class DistrictListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterDistrict
        fields = (
            MasterDistrictFields.ID, MasterDistrictFields.NAME, MasterDistrictFields.CITY
        )
