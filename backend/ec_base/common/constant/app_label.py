from ..utils.utils import BaseEnum


class ModelAppLabel(str, BaseEnum):
    USER_INFO = 'user_info'
    STAFF = 'staff'
    CUSTOMER = 'customer'
    MASTER = 'master'
    DISCOUNT = 'discount'
