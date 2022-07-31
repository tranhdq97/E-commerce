from rest_framework import serializers

from ..models.sex import MasterSex
from ...common.constant.db_fields import CommonFields, MasterFields


class MasterSexSlz(serializers.ModelSerializer):
    class Meta:
        model = MasterSex
        fields = (CommonFields.ID, MasterFields.NAME,)
