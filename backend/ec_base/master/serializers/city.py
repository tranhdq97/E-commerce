from rest_framework import serializers

from ec_base.common.constant.db_fields import CommonFields, MasterFields
from ec_base.master.models.district import MasterCity


class MasterCitySlz(serializers.ModelSerializer):
    class Meta:
        model = MasterCity
        fields = (CommonFields.ID, MasterFields.NAME)
