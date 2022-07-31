from ..utils.utils import BaseEnum


class MasterStaffID(int, BaseEnum):
    EMPLOYEE = 1
    SUPER_STAFF = 2
    MANAGER = 3
    UNAPPROVED = 4
