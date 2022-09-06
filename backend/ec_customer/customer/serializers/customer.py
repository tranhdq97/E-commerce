from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from ec_base.common.constant import message
from ec_base.common.constant.constant import RegexPattern
from ec_base.common.constant.db_fields import CommonFields, UserFields
from ec_base.common.utils.exceptions import APIErr
from ec_base.common.utils.strings import check_regex
from ec_base.customer.models.customer import Customer
from ec_base.user_info.serializers.user_info import UserInfoUpdateSlz


class CustomerBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (CommonFields.ID,)


class CustomerUpdateSlz(CustomerBaseSlz, WritableNestedModelSerializer):
    info = UserInfoUpdateSlz(many=False)

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (UserFields.INFO,)


class CustomerCreateSlz(CustomerBaseSlz):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (UserFields.EMAIL, UserFields.PASSWORD,)

    def validate(self, attrs):
        email = attrs.get(UserFields.EMAIL)
        password = attrs.get(UserFields.PASSWORD)
        if self.Meta.model.objects.filter(email=email).exists():
            raise APIErr(message.ALREADY_EXISTS)

        if not check_regex(RegexPattern.PASSWORD, password):
            raise APIErr(message.PASSWORD_INAPPROPRIATE)

        if email == password:
            raise APIErr(message.PASSWORD_MUST_DIFFER_EMAIL)

        return attrs

    def create(self, validated_data):
        customer = self.Meta.model.objects.create_user(**validated_data)
        return customer
