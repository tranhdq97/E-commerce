from rest_framework import serializers

from ec_base.common.constant.db_fields import CommonFields
from ec_base.order_item.models import OrderItem


class OrderItemBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (CommonFields.ID,)
