from ..utils.utils import BaseEnum


class DBTable(str, BaseEnum):
    # Master tables
    MASTER_SEX = 'master_sex'
    MASTER_STAFF_TYPE = 'master_staff_type'
    MASTER_CITY = 'master_city'
    MASTER_DISTRICT = 'master_district'
    MASTER_PRODUCT_CATEGORY = 'master_product_category'
    MASTER_DISCOUNT_TYPE = 'master_discount_type'
