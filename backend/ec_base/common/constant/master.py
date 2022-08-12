from ..utils.utils import BaseEnum


class MasterStaffID(int, BaseEnum):
    EMPLOYEE = 1
    SUPER_STAFF = 2
    MANAGER = 3
    UNAPPROVED = 4


class MasterFileTypeID(int, BaseEnum):
    IMAGE = 1
    DOCUMENT = 2
    VIDEO = 3
    PRESENTATION = 4
    AUDIO = 5
    ANY = 6
