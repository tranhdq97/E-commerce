from rest_framework import serializers

from ec_base.common.constant.db_fields import CommonFields, UserFields
from ec_base.customer.models import Customer
from ec_base.user_info.serializers.user_info import UserInfoBaseSlz, UserInfoRetrieveSlz


class CustomerBaseSlz(serializers.ModelSerializer):
    info = UserInfoBaseSlz(many=False)

    class Meta:
        model = Customer
        fields = (CommonFields.ID, UserFields.EMAIL, UserFields.INFO, CommonFields.CREATED_AT, CommonFields.UPDATED_AT)
