from rest_framework import serializers

from ..models import Discount
from ...common.constant import message
from ...common.constant.db_fields import CommonFields, DiscountFields
from ...common.utils.serializer import ForeignKeyField
from ...master.models import MasterDiscountType, MasterDiscountRate
from ...master.serializers.discount_rate import MasterDiscountRateSlz
from ...master.serializers.discount_type import MasterDiscountTypeSlz


class DiscountBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = (CommonFields.ID,)

    def validate_discount_type_id(self, discount_type_id):
        if DiscountBaseSlz.Meta.model.objects.filter(is_deleted=False, discount_type_id=discount_type_id).exists():
            raise ValueError(message.DUPLICATE_ENTRY)

        return discount_type_id


class DiscountListSlz(DiscountBaseSlz):
    discount_type = MasterDiscountTypeSlz(many=False)
    discount_rate = MasterDiscountRateSlz(many=False)

    class Meta:
        model = DiscountBaseSlz.Meta.model
        fields = DiscountBaseSlz.Meta.fields + (DiscountFields.DISCOUNT_TYPE, DiscountFields.DISCOUNT_RATE)


class DiscountRetrieveSlz(DiscountBaseSlz):
    discount_type = MasterDiscountTypeSlz(many=False)
    discount_rate = MasterDiscountRateSlz(many=False)

    class Meta:
        model = DiscountBaseSlz.Meta.model
        fields = DiscountBaseSlz.Meta.fields + (DiscountFields.DISCOUNT_TYPE, DiscountFields.DISCOUNT_RATE,) + (
            CommonFields.CREATED_BY_ID, CommonFields.UPDATED_BY_ID, CommonFields.CREATED_AT, CommonFields.UPDATED_AT)


class DiscountCreateSlz(DiscountBaseSlz):
    discount_type_id = ForeignKeyField(model=MasterDiscountType)
    discount_rate_id = ForeignKeyField(model=MasterDiscountRate)

    class Meta:
        model = DiscountBaseSlz.Meta.model
        fields = DiscountBaseSlz.Meta.fields + (DiscountFields.DISCOUNT_TYPE_ID, DiscountFields.DISCOUNT_RATE_ID) + (
            CommonFields.CREATED_AT,)


class DiscountUpdateSlz(DiscountBaseSlz):
    discount_type_id = ForeignKeyField(model=MasterDiscountType)
    discount_rate_id = ForeignKeyField(model=MasterDiscountRate)

    class Meta:
        model = DiscountBaseSlz.Meta.model
        fields = DiscountBaseSlz.Meta.fields + (DiscountFields.DISCOUNT_TYPE_ID, DiscountFields.DISCOUNT_RATE_ID) + (
            CommonFields.UPDATED_AT,)
