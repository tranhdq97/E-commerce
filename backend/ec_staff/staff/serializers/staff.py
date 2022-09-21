from django.db import transaction
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from ec_base.common.constant import message
from ec_base.common.constant.constant import RegexPattern
from ec_base.common.constant.db_fields import CommonFields, UserFields
from ec_base.common.utils.exceptions import APIErr
from ec_base.common.utils.strings import check_regex
from ec_base.staff.models.staff import Staff
from ec_base.user_info.models.user_info import UserInfo
from ec_base.user_info.serializers.user_info import UserInfoCreateSlz, UserInfoUpdateSlz


class StaffBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (CommonFields.ID,)


class StaffUpdateSlz(StaffBaseSlz, WritableNestedModelSerializer):
    info = UserInfoUpdateSlz(many=False)

    class Meta:
        model = StaffBaseSlz.Meta.model
        fields = StaffBaseSlz.Meta.fields + (UserFields.INFO,)


class StaffCreateSlz(StaffBaseSlz):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    info = UserInfoCreateSlz(many=False)

    class Meta:
        model = StaffBaseSlz.Meta.model
        fields = StaffBaseSlz.Meta.fields + (
            UserFields.EMAIL,
            UserFields.PASSWORD,
            UserFields.INFO,
        )

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
        with transaction.atomic():
            info = validated_data.get(UserFields.INFO)
            validated_data[UserFields.INFO] = UserInfo.objects.create(**info)
            staff = self.Meta.model.objects.create_user(**validated_data)
            return staff
