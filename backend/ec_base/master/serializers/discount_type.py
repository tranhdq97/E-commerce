from rest_framework import serializers

from ..models.discount_type import MasterDiscountType
from ...common.constant.db_fields import CommonFields, MasterFields


class MasterDiscountTypeSlz(serializers.ModelSerializer):
    class Meta:
        model = MasterDiscountType
        fields = (CommonFields.ID, MasterFields.NAME)
