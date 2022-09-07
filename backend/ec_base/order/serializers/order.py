from rest_framework import serializers

from ec_base.common.constant.db_fields import CommonFields
from ec_base.order.models.order import Order


class OrderBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (CommonFields.ID,)
