from rest_framework import serializers

from ..models import Staff
from ...common.constant.db_fields import StaffFields, CommonFields
from ...user_info.serializers.user_info import UserInfoRetrieveSlz


class StaffInfoSlz(serializers.ModelSerializer):
    info = UserInfoRetrieveSlz(many=False)

    class Meta:
        model = Staff
        fields = (CommonFields.ID, StaffFields.INFO)
