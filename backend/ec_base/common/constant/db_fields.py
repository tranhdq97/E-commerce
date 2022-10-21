from ec_base.common.utils.utils import BaseEnum


# --------------------------------------  Common
class CommonFields(str, BaseEnum):
    ID = "id"
    USER = "user"
    IS_DELETED = "is_deleted"
    FILTER_BY = 'filter_by'
    FILTER_BY_ID = 'filter_by_id'
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    CREATED_BY = "created_by"
    CREATED_BY_ID = "created_by_id"
    UPDATED_BY = "updated_by"
    UPDATED_BY_ID = "updated_by_id"


# --------------------------------------  Master
class MasterFields(str, BaseEnum):
    NAME = "name"
    PARENT_ID = "parent_id"


class MasterDistrictFields(str, BaseEnum):
    CITY = "city"
    CITY_ID = "city_id"


class MasterProductCategoryFields(str, BaseEnum):
    QUANTITY = 'quantity'
    AMOUNT = 'amount'


# --------------------------------------  Others
class UserInfoFields(str, BaseEnum):
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    DOB = "dob"
    SEX = "sex"
    SEX_ID = "sex_id"
    CITY = "city"
    CITY_ID = "city_id"
    DISTRICT = "district"
    DISTRICT_ID = "district_id"
    BUILDING = "building"
    POSTAL_CODE = "postal_code"
    PHONE_NUMBER = "phone_number"
    PHOTO = "photo"
    PHOTO_ID = "photo_id"


class UserFields(str, BaseEnum):
    INFO = "info"
    INFO_ID = "info_id"
    TYPE = "type"
    TYPE_ID = "type_id"
    EMAIL = "email"
    PASSWORD = "password"
    NEW_PASSWORD = "new_password"
    IS_ACTIVATE = "is_activate"
    IS_LEAVE = "is_leave"
    IS_ADMIN = "is_admin"
    LAST_LOGIN = "last_login"


class DiscountFields(str, BaseEnum):
    DISCOUNT_TYPE = "discount_type"
    DISCOUNT_TYPE_ID = "discount_type_id"
    DISCOUNT_RATE = "discount_rate"
    DISCOUNT_RATE_ID = "discount_rate_id"
    IS_DELETED = "is_deleted"


class FileManagementFields(str, BaseEnum):
    NAME = "name"
    DESC = "desc"
    FILE = "file"
    TYPE = "type"
    TYPE_ID = "type_id"
    IS_DELETED = "is_deleted"


class RatingFields(str, BaseEnum):
    COMMENT = "comment"
    NUM_STARS = "num_stars"
    MEDIA = "media"
    MEDIA_ID = "media_id"
    PRODUCT = "product"
    PRODUCT_ID = "product_id"


class ProductFields(str, BaseEnum):
    NAME = "name"
    CATEGORY = "category"
    CATEGORY_ID = "category_id"
    QUANTITY = "quantity"
    PURCHASE_PRICE = "purchase_price"
    PRICE = "price"
    PHOTO = "photo"
    PHOTO_ID = "photo_id"
    DESC = "desc"
    IS_DELETED = "is_deleted"


class OrderFields(str, BaseEnum):
    STATUS = "status"
    STATUS_ID = "status_id"
    SHIPPING_STATUS = "shipping_status"
    SHIPPING_STATUS_ID = "shipping_status_id"
    PAYMENT_STATUS = "payment_status"
    PAYMENT_STATUS_ID = "payment_status_id"
    ORDER_ITEMS = "order_items"


class OrderItemFields(str, BaseEnum):
    ORDER = "order"
    ORDER_ID = "order_id"
    PRODUCT = "product"
    PRODUCT_ID = "product_id"
    QUANTITY = "quantity"
    DISCOUNTS = "discounts"
    ACTUAL_AMOUNT = "actual_amount"
    TOTAL_QUANTITY = 'total_quantity'
    TOTAL_AMOUNT = 'total_amount'
