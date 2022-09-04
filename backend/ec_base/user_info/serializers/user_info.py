from rest_framework import serializers

from ec_base.common.constant.db_fields import UserInfoFields, CommonFields
from ec_base.common.utils.serializer import ForeignKeyField
from ec_base.file_management.models import FileManagement
from ec_base.file_management.serializers.file_management import FileManagementPthSlz
from ec_base.master.models import MasterSex, MasterCity, MasterDistrict
from ec_base.master.serializers import MasterCitySlz, MasterSexSlz, MasterDistrictSlz
from ec_base.user_info.models.user_info import UserInfo


class UserInfoBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = (CommonFields.ID, UserInfoFields.FIRST_NAME, UserInfoFields.LAST_NAME, UserInfoFields.DOB,
                  UserInfoFields.PHONE_NUMBER)


class UserInfoCreateSlz(UserInfoBaseSlz):
    sex_id = ForeignKeyField(model=MasterSex, required=False)
    city_id = ForeignKeyField(model=MasterCity, required=False)
    district_id = ForeignKeyField(model=MasterDistrict, required=False)
    photo_id = ForeignKeyField(model=FileManagement, required=False)

    class Meta:
        model = UserInfoBaseSlz.Meta.model
        fields = UserInfoBaseSlz.Meta.fields + (
            UserInfoFields.SEX_ID, UserInfoFields.CITY_ID, UserInfoFields.DISTRICT_ID, UserInfoFields.PHOTO_ID,)
        read_only_fields = (CommonFields.ID,)


class UserInfoUpdateSlz(UserInfoBaseSlz):
    sex_id = ForeignKeyField(model=MasterSex, required=False)
    city_id = ForeignKeyField(model=MasterCity, required=False)
    district_id = ForeignKeyField(model=MasterDistrict, required=False)
    photo_id = ForeignKeyField(model=FileManagement, required=False)

    class Meta:
        model = UserInfoBaseSlz.Meta.model
        fields = UserInfoBaseSlz.Meta.fields + (
            UserInfoFields.SEX_ID, UserInfoFields.CITY_ID, UserInfoFields.DISTRICT_ID, UserInfoFields.PHOTO_ID,)


class UserInfoRetrieveSlz(UserInfoBaseSlz):
    sex = MasterSexSlz(many=False)
    city = MasterCitySlz(many=False)
    district = MasterDistrictSlz(many=False)
    photo = FileManagementPthSlz(many=False)

    class Meta:
        model = UserInfoBaseSlz.Meta.model
        fields = UserInfoBaseSlz.Meta.fields + (
            UserInfoFields.SEX, UserInfoFields.CITY, UserInfoFields.DISTRICT, UserInfoFields.PHOTO,
            UserInfoFields.PHOTO_ID,
        ) + (CommonFields.CREATED_AT, CommonFields.UPDATED_AT)


class UserInfoListSlz(UserInfoBaseSlz):
    class Meta:
        model = UserInfoBaseSlz.Meta.model
        fields = UserInfoBaseSlz.Meta.fields
