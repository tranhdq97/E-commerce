from rest_framework import serializers

from ..models.user_info import UserInfo
from ...common.constant.db_fields import UserInfoFields, CommonFields
from ...common.utils.serializer import ForeignKeyField
from ...master.models import MasterSex, MasterCity, MasterDistrict
from ...master.serializers import MasterCitySlz, MasterSexSlz, MasterDistrictSlz


class UserInfoBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = (CommonFields.ID, UserInfoFields.FIRST_NAME, UserInfoFields.LAST_NAME, UserInfoFields.DOB,
                  UserInfoFields.BUILDING, UserInfoFields.POSTAL_CODE, UserInfoFields.PHONE_NUMBER)


class UserInfoCreateSlz(UserInfoBaseSlz):
    sex_id = ForeignKeyField(model=MasterSex)
    city_id = ForeignKeyField(model=MasterCity)
    district_id = ForeignKeyField(model=MasterDistrict)

    class Meta:
        model = UserInfoBaseSlz.Meta.model
        fields = UserInfoBaseSlz.Meta.fields + (
            UserInfoFields.SEX_ID, UserInfoFields.CITY_ID, UserInfoFields.DISTRICT_ID)
        read_only_fields = (CommonFields.ID,)


class UserInfoUpdateSlz(UserInfoBaseSlz):
    sex_id = ForeignKeyField(model=MasterSex)
    city_id = ForeignKeyField(model=MasterCity)
    district_id = ForeignKeyField(model=MasterDistrict)

    class Meta:
        model = UserInfoBaseSlz.Meta.model
        fields = UserInfoBaseSlz.Meta.fields + (
            UserInfoFields.SEX_ID, UserInfoFields.CITY_ID, UserInfoFields.DISTRICT_ID)


class UserInfoRetrieveSlz(UserInfoBaseSlz):
    sex = MasterSexSlz(many=False)
    city = MasterCitySlz(many=False)
    district = MasterDistrictSlz(many=False)

    class Meta:
        model = UserInfoBaseSlz.Meta.model
        fields = UserInfoBaseSlz.Meta.fields + (UserInfoFields.SEX, UserInfoFields.CITY, UserInfoFields.DISTRICT,) + (
            CommonFields.CREATED_AT, CommonFields.UPDATED_AT)


class UserInfoListSlz(UserInfoBaseSlz):
    sex = MasterSexSlz(many=False)
    city = MasterCitySlz(many=False)
    district = MasterDistrictSlz(many=False)

    class Meta:
        model = UserInfoBaseSlz.Meta.model
        fields = UserInfoBaseSlz.Meta.fields + (UserInfoFields.SEX, UserInfoFields.CITY, UserInfoFields.DISTRICT,)
