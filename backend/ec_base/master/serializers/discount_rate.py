from rest_framework import serializers

from ..models.discount_rate import MasterDiscountRate
from ...common.constant.db_fields import CommonFields, MasterFields


class MasterDiscountRateSlz(serializers.ModelSerializer):
    class Meta:
        model = MasterDiscountRate
        fields = (CommonFields.ID, MasterFields.NAME)
