from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from ..models.customer import Customer
from ...common.constant.db_fields import CommonFields, CustomerFields
from ...user_info.serializers.user_info import UserInfoCreateSlz, UserInfoUpdateSlz, UserInfoRetrieveSlz, \
    UserInfoListSlz


class CustomerBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (CommonFields.ID,)


class CustomerListSlz(CustomerBaseSlz):
    info = UserInfoListSlz(many=False)

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (CustomerFields.INFO,)


class CustomerRetrieveSlz(CustomerBaseSlz):
    info = UserInfoRetrieveSlz(many=False)

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (CustomerFields.INFO,)


class CustomerUpdateSlz(CustomerBaseSlz, WritableNestedModelSerializer):
    info = UserInfoUpdateSlz(many=False)

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (CustomerFields.INFO,) + (
            CommonFields.CREATED_BY_ID, CommonFields.UPDATED_BY_ID)
        read_only_fields = (CommonFields.ID, CommonFields.CREATED_BY_ID, CommonFields.UPDATED_BY_ID,)


class CustomerCreateSlz(CustomerBaseSlz, WritableNestedModelSerializer):
    info = UserInfoCreateSlz(many=False)

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (CustomerFields.INFO,) + (
            CommonFields.CREATED_BY_ID, CommonFields.UPDATED_BY_ID)
        read_only_fields = (CommonFields.ID, CommonFields.CREATED_BY_ID, CommonFields.UPDATED_BY_ID,)
