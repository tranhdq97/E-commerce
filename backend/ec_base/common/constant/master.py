from ec_base.common.utils.utils import BaseEnum


class MasterStaffTypeID(int, BaseEnum):
    SUPER_STAFF = 1
    MANAGER = 2
    EMPLOYEE = 3
    UNAPPROVED = 4


class MasterCustomerTypeID(int, BaseEnum):
    UNVERIFIED = 1
    VERIFIED = 2


class MasterFileTypeID(int, BaseEnum):
    IMAGE = 1
    DOCUMENT = 2
    VIDEO = 3
    PRESENTATION = 4
    AUDIO = 5
    ANY = 6


class MasterOrderStatusID(int, BaseEnum):
    ORDERED = 1
    CANCELED = 2


class MasterShippingStatusID(int, BaseEnum):
    UNDELIVERED = 1
    DELIVERING = 2
    DELIVERED = 3


class MasterPaymentStatusID(int, BaseEnum):
    UNPAID = 1
    PAID = 2


class MasterFilterByID(int, BaseEnum):
    TODAY = 1
    THIS_MONTH = 2
    THIS_YEAR = 3
    LAST_FIVE_YEARS = 4
