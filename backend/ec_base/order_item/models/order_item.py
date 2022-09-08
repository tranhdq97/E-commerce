from django.db import models

from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_table import DBTable
from ec_base.common.constant.related_name import RelatedName
from ec_base.discount.models import Discount
from ec_base.order.models.order import Order
from ec_base.product.models import Product


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.RESTRICT, related_name=DBTable.ORDER_ITEM)
    product = models.ForeignKey(to=Product, on_delete=models.RESTRICT, related_name=DBTable.ORDER_ITEM)
    quantity = models.IntegerField()
    discounts = models.ManyToManyField(to=Discount, related_name=RelatedName.ORDER_ITEMS)

    class Meta:
        db_table = DBTable.ORDER_ITEM
        app_label = ModelAppLabel.ORDER_ITEM
