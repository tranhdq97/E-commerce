from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from ...common.constant import message
from ...common.constant.constant import RegexPattern
from ...common.constant.db_fields import CommonFields, StaffFields
from ...common.custom.exceptions import APIErr
from ...common.utils.strings import check_regex


class ForgetPasswordSlz(serializers.Serializer):
    # TODO: Send an email helping user change password
    pass


class ChangePasswordSlz(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, new_password):
        user = self.context.get(CommonFields.USER)
        if not check_regex(RegexPattern.PASSWORD, new_password):
            raise APIErr(message.PASSWORD_FAILED)

        if new_password == user.email:
            raise APIErr(message.PASSWORD_IDENTICAL_AS_EMAIL)

        return new_password

    def validate_old_password(self, old_password):
        user = self.context.get(CommonFields.USER)
        if not user.check_password(old_password):
            raise APIErr(message.PASSWORD_DID_NOT_MATCH)

        return old_password

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data.get(StaffFields.NEW_PASSWORD))
        instance.save()
        return instance
