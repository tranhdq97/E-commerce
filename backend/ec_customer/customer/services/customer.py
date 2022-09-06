from ec_base.common.constant.db_fields import UserFields, CommonFields
from ec_base.common.utils.decorator import log
from ec_base.customer.services import BaseCustomerSvc
from ec_customer.customer.serializers.customer import CustomerUpdateSlz


class CustomerSvc(BaseCustomerSvc):
    """Customer service."""

    @log
    def update_customer(self, pk, data):
        instance = self.get_customer(pk)
        if instance.info_id and data.get(UserFields.INFO) is not None:
            data[UserFields.INFO][CommonFields.ID] = instance.info_id

        slz = CustomerUpdateSlz(instance=instance, data=data, partial=True)
        slz.is_valid(raise_exception=True)
        slz.save()
        return slz
