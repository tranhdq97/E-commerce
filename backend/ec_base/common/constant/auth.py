from django.core.exceptions import ImproperlyConfigured

from ec_base.common.constant import message
from ec_base.common.utils.utils import BaseEnum
from ec_base.customer.models import Customer
from ec_base.staff.models import Staff


class UserEnum(str, BaseEnum):
    PROVIDER = 'provider'
    CUSTOMER = 'customer'
    STAFF = 'staff'
    EMAIL = 'email'


def get_user_model_by_provider(provider=UserEnum.STAFF):
    user_model_switcher = {
        UserEnum.CUSTOMER: Customer,
        UserEnum.STAFF: Staff,
    }
    user_model = user_model_switcher.get(provider)
    if user_model is None:
        raise ImproperlyConfigured(message.INVALID_PROVIDER)

    return user_model
