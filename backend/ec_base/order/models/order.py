from django.db import models

from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_table import DBTable
from ec_base.common.models.base import CustomerCreator, DateTimeModel, CustomerEditor
from ec_base.master.models import MasterOrderStatus, MasterShippingStatus, MasterPaymentStatus


class Order(CustomerCreator, CustomerEditor, DateTimeModel):
    status = models.ForeignKey(to=MasterOrderStatus, on_delete=models.RESTRICT, related_name=DBTable.ORDER)
    shipping_status = models.ForeignKey(to=MasterShippingStatus, on_delete=models.RESTRICT, related_name=DBTable.ORDER)
    payment_status = models.ForeignKey(to=MasterPaymentStatus, on_delete=models.RESTRICT, related_name=DBTable.ORDER)

    class Meta:
        db_table = DBTable.ORDER
        app_label = ModelAppLabel.ORDER
