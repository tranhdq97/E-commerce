import logging

from ..serializers.auth import ChangePasswordSlz
from ...common.constant import message
from ...staff.serializers.staff import StaffInfoSlz
from ...common.utils.decorator import log

logger = logging.getLogger(__name__)


class AuthSvc:
    @staticmethod
    def change_password(user, data):
        logger.info(f'START | change_password')
        slz = ChangePasswordSlz(data=data, context=dict(user=user))
        slz.is_valid(raise_exception=True)
        slz.update(user, data)
        logger.info(f'END   | change_password')
        return dict(massage=message.PASSWORD_CHANGE_SUCCESSFUL)

    @staticmethod
    @log
    def get_me(user):
        slz = StaffInfoSlz(user)
        return slz.data
