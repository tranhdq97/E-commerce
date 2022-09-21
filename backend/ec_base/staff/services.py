from ec_base.common.constant import message
from ec_base.common.utils.exceptions import APIErr
from ec_base.staff.models import Staff


class BaseStaffSvc:
    """Staff service."""

    @staticmethod
    def get_staff(pk):
        try:
            return Staff.objects.get(pk=pk)
        except Staff.DoesNotExist:
            raise APIErr(message.NOT_EXIST)
