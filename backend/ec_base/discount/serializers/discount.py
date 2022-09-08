from rest_framework import serializers

from ec_base.common.constant import message
from ec_base.common.constant.db_fields import CommonFields
from ec_base.common.utils.exceptions import APIErr
from ec_base.discount.models import Discount


class DiscountBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = (CommonFields.ID,)

    def validate_discount_type_id(self, discount_type_id):
        if DiscountBaseSlz.Meta.model.objects.filter(is_deleted=False, discount_type_id=discount_type_id).exists():
            raise APIErr(message.DUPLICATE_ENTRY)

        return discount_type_id
