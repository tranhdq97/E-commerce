from rest_framework import serializers

from ec_base.common.constant.db_fields import MasterProductCategoryFields, CommonFields, MasterFields
from ec_base.master.models import MasterProductCategory


class OverviewReqParams(serializers.Serializer):
    filter_by_id = serializers.IntegerField(required=True)


class SaleQuantityOverviewListSlz(serializers.ModelSerializer):
    quantity = serializers.IntegerField()

    class Meta:
        model = MasterProductCategory
        fields = (CommonFields.ID, MasterFields.NAME, MasterProductCategoryFields.QUANTITY,)


class SaleAmountOverviewListSlz(serializers.ModelSerializer):
    amount = serializers.FloatField()

    class Meta:
        model = MasterProductCategory
        fields = (CommonFields.ID, MasterFields.NAME, MasterProductCategoryFields.AMOUNT,)
