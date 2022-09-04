from rest_framework import serializers

from ec_base.common.constant.db_fields import CommonFields, MasterDistrictFields
from ec_base.master.models.district import MasterDistrict


class MasterDistrictSlz(serializers.ModelSerializer):
    class Meta:
        model = MasterDistrict
        fields = (CommonFields.ID, MasterDistrictFields.NAME, MasterDistrictFields.CITY)


class MasterDistrictCreateSlz(serializers.ModelSerializer):
    class Meta:
        model = MasterDistrict
        fields = (CommonFields.ID, MasterDistrictFields.NAME, MasterDistrictFields.CITY)
        read_only_fields = (CommonFields.ID,)
