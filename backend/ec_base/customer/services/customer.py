from ..models import Customer
from ..serializers.customer import CustomerUpdateSlz
from ...common.constant.db_fields import CustomerFields, CommonFields


class CustomerSvc:
    """Customer service."""

    @staticmethod
    def get_customer(pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise ValueError('Customer does not exist')

    def update_customer(self, pk, data):
        instance = self.get_customer(pk)
        if instance.info_id and data.get(CustomerFields.INFO) is not None:
            data[CustomerFields.INFO][CommonFields.ID] = instance.info_id

        slz = CustomerUpdateSlz(instance=instance, data=data, partial=True)
        slz.is_valid(raise_exception=True)
        slz.save()
        return slz
