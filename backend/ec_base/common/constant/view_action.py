from ..utils.utils import BaseEnum


class BaseViewAction(str, BaseEnum):
    LIST = 'list'
    RETRIEVE = 'retrieve'
    CREATE = 'create'
    UPDATE = 'update'
    DESTROY = 'destroy'
