from rest_framework import status
from rest_framework.exceptions import APIException

from ec_base.common.constant import message


class APIErr(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = message.INVALID_INPUT
    default_code = '400'


class PermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = message.PERMISSION_DENIED
    default_code = '403'
