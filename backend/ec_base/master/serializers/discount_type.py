from rest_framework import serializers

from ec_base.common.constant.db_fields import CommonFields, MasterFields
from ec_base.master.models.discount_type import MasterDiscountType


class MasterDiscountTypeSlz(serializers.ModelSerializer):
    class Meta:
        model = MasterDiscountType
        fields = (CommonFields.ID, MasterFields.NAME)
