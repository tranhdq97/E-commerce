from ec_base.common.constant import message
from ec_base.common.utils.exceptions import APIErr
from ec_base.customer.models import Customer


class BaseCustomerSvc:
    """Customer service."""

    @staticmethod
    def get_customer(pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise APIErr(message.NOT_EXIST)
