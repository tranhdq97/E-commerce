import logging

from ec_base.auth.serializers.auth import ChangePasswordSlz
from ec_base.common.constant import message
from ec_base.common.constant.auth import UserEnum
from ec_base.common.utils.decorator import log
from ec_base.customer.serializers.customer import CustomerRetrieveSlz
from ec_base.staff.serializers.staff import StaffRetrieveSlz

logger = logging.getLogger(__name__)


class AuthSvc:
    @staticmethod
    def change_password(user, data):
        logger.info("START | change_password")
        slz = ChangePasswordSlz(data=data, context=dict(user=user))
        slz.is_valid(raise_exception=True)
        slz.update(user, data)
        logger.info("END   | change_password")
        return dict(massage=message.PASSWORD_CHANGE_SUCCESSFUL)

    @staticmethod
    @log
    def get_me(user):
        slz_switcher = {
            UserEnum.CUSTOMER: CustomerRetrieveSlz,
            UserEnum.STAFF: StaffRetrieveSlz,
        }
        slz = slz_switcher.get(user.provider)(user)
        return slz.data
