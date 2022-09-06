from rest_framework import serializers

from ec_base.common.constant.db_fields import CommonFields, MasterFields
from ec_base.master.models.discount_rate import MasterDiscountRate


class MasterDiscountRateSlz(serializers.ModelSerializer):
    class Meta:
        model = MasterDiscountRate
        fields = (CommonFields.ID, MasterFields.NAME)
