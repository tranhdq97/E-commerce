from ..utils.utils import BaseEnum


class MasterFields(str, BaseEnum):
    ID = 'id'
    NAME = 'name'
    IS_DELETED = 'is_deleted'
    PARENT_ID = 'parent_id'


class MasterDistrictFields(str, BaseEnum):
    ID = 'id'
    NAME = 'name'
    IS_DELETED = 'is_deleted'
    CITY = 'city'
    CITY_ID = 'city_id'
