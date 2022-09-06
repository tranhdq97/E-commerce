from rest_framework import serializers

from ec_base.common.constant.db_fields import CommonFields, UserFields
from ec_base.customer.models.customer import Customer
from ec_base.user_info.serializers.user_info import UserInfoRetrieveSlz, \
    UserInfoListSlz


class CustomerBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (CommonFields.ID,)


class CustomerListSlz(CustomerBaseSlz):
    info = UserInfoListSlz(many=False)

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (UserFields.EMAIL, UserFields.INFO,)


class CustomerRetrieveSlz(CustomerBaseSlz):
    info = UserInfoRetrieveSlz(many=False)

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (UserFields.INFO,)
