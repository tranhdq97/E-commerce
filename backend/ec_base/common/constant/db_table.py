from ..utils.utils import BaseEnum


class DBTable(str, BaseEnum):
    # Master tables
    MASTER = 'master'
    MASTER_SEX = 'm_sex'
    MASTER_STAFF_TYPE = 'm_staff_type'
    MASTER_CITY = 'm_city'
    MASTER_DISTRICT = 'm_district'
    MASTER_PRODUCT_CATEGORY = 'm_product_category'
    MASTER_DISCOUNT_TYPE = 'm_discount_type'

    STAFF = 'staff'
    USER_INFO = 'user_info'
