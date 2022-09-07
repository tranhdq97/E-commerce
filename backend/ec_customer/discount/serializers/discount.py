from ec_base.common.constant.db_fields import CommonFields, DiscountFields
from ec_base.common.utils.serializer import ForeignKeyField
from ec_base.discount.serializers.discount import DiscountBaseSlz
from ec_base.master.models import MasterDiscountType, MasterDiscountRate
from ec_base.master.serializers.discount_rate import MasterDiscountRateSlz
from ec_base.master.serializers.discount_type import MasterDiscountTypeSlz


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


class DiscountForOrderItemRetrieveSlz(DiscountBaseSlz):
    discount_type = MasterDiscountTypeSlz(many=False)
    discount_rate = MasterDiscountRateSlz(many=False)

    class Meta:
        model = DiscountBaseSlz.Meta.model
        fields = DiscountBaseSlz.Meta.fields + (DiscountFields.DISCOUNT_TYPE, DiscountFields.DISCOUNT_RATE)
