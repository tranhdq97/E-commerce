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
