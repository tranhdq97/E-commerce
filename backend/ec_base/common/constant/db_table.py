from ec_base.common.utils.utils import BaseEnum


class DBTable(str, BaseEnum):
    # Master tables
    MASTER = 'master'
    MASTER_SEX = 'm_sex'
    MASTER_STAFF_TYPE = 'm_staff_type'
    MASTER_CITY = 'm_city'
    MASTER_DISTRICT = 'm_district'
    MASTER_PRODUCT_CATEGORY = 'm_product_category'
    MASTER_DISCOUNT_TYPE = 'm_discount_type'
    MASTER_DISCOUNT_RATE = 'm_discount_rate'
    MASTER_FILE_TYPE = 'm_file_type'
    MASTER_ORDER_STATUS = 'm_order_status'
    MASTER_SHIPPING_STATUS = 'm_shipping_status'
    MASTER_PAYMENT_STATUS = 'm_payment_status'
    MASTER_CUSTOMER_TYPE = 'm_customer_type'

    STAFF = 'staff'
    USER_INFO = 'user_info'
    CUSTOMER = 'customer'
    DISCOUNT = 'discount'
    PRODUCT = 'product'
    FILE_MANAGEMENT = 'file_management'
    RATING = 'rating'
