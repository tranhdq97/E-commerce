from ec_base.common.utils.utils import BaseEnum


class BaseViewAction(str, BaseEnum):
    LIST = 'list'
    RETRIEVE = 'retrieve'
    CREATE = 'create'
    UPDATE = 'update'
    DESTROY = 'destroy'


class OrderViewAction(str, BaseEnum):
    CANCEL = 'cancel'
