from ..utils.utils import BaseEnum


# --------------------------------------  Common
class CommonFields(str, BaseEnum):
    ID = 'id'
    USER = 'user'
    IS_DELETED = 'is_deleted'
    CREATED_AT = 'created_at'
    UPDATED_AT = 'updated_at'
    CREATED_BY = 'created_by'
    CREATED_BY_ID = 'created_by_id'
    UPDATED_BY = 'updated_by'
    UPDATED_BY_ID = 'updated_by_id'


# --------------------------------------  Master
class MasterFields(str, BaseEnum):
    NAME = 'name'
    PARENT_ID = 'parent_id'


class MasterDistrictFields(str, BaseEnum):
    NAME = 'name'
    CITY = 'city'
    CITY_ID = 'city_id'


# --------------------------------------  Others
class UserInfoFields(str, BaseEnum):
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    DOB = 'dob'
    SEX = 'sex'
    SEX_ID = 'sex_id'
    CITY = 'city'
    CITY_ID = 'city_id'
    DISTRICT = 'district'
    DISTRICT_ID = 'district_id'
    BUILDING = 'building'
    POSTAL_CODE = 'postal_code'
    PHONE_NUMBER = 'phone_number'


class CustomerFields(str, BaseEnum):
    INFO = 'info'
    INFO_ID = 'info_id'


class StaffFields(str, BaseEnum):
    INFO = 'info'
    INFO_ID = 'info_id'
    TYPE = 'type'
    TYPE_ID = 'type_id'
    EMAIL = 'email'
    PASSWORD = 'password'
    NEW_PASSWORD = 'new_password'
    IS_ACTIVATE = 'is_activate'
    IS_LEAVE = 'is_leave'
    IS_ADMIN = 'is_admin'
    LAST_LOGIN = 'last_login'


class DiscountFields(str, BaseEnum):
    DISCOUNT_TYPE = 'discount_type'
    DISCOUNT_TYPE_ID = 'discount_type_id'
    DISCOUNT_RATE = 'discount_rate'
    DISCOUNT_RATE_ID = 'discount_rate_id'
    IS_DELETED = 'is_deleted'
