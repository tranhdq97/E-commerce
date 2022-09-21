from ec_base.common.constant.db_fields import UserFields, CommonFields
from ec_base.common.utils.decorator import log
from ec_base.staff.services import BaseStaffSvc
from ec_staff.staff.serializers.staff import StaffUpdateSlz


class StaffSvc(BaseStaffSvc):
    """Staff service."""

    @log
    def update_staff(self, pk, data):
        instance = self.get_staff(pk)
        if instance.info_id and data.get(UserFields.INFO) is not None:
            data[UserFields.INFO][CommonFields.ID] = instance.info_id

        slz = StaffUpdateSlz(instance=instance, data=data, partial=True)
        slz.is_valid(raise_exception=True)
        slz.save()
        return slz
