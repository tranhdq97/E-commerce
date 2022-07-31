from rest_framework import serializers

from ..models.district import MasterCity
from ...common.constant.db_fields import CommonFields, MasterFields


class MasterCitySlz(serializers.ModelSerializer):
    class Meta:
        model = MasterCity
        fields = (CommonFields.ID, MasterFields.NAME)
