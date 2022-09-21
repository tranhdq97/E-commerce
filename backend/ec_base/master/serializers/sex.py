from rest_framework import serializers

from ec_base.common.constant.db_fields import CommonFields, MasterFields
from ec_base.master.models.sex import MasterSex


class MasterSexSlz(serializers.ModelSerializer):
    class Meta:
        model = MasterSex
        fields = (
            CommonFields.ID,
            MasterFields.NAME,
        )
