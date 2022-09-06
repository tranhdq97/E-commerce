from rest_framework import serializers

from ec_base.common.constant.db_fields import UserFields, CommonFields
from ec_base.staff.models import Staff
from ec_base.user_info.serializers.user_info import UserInfoRetrieveSlz


class StaffRetrieveSlz(serializers.ModelSerializer):
    info = UserInfoRetrieveSlz(many=False)

    class Meta:
        model = Staff
        fields = (CommonFields.ID, UserFields.EMAIL, UserFields.INFO, CommonFields.CREATED_AT, CommonFields.UPDATED_AT)
