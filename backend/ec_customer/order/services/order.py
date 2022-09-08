from django.db import transaction

from ec_base.common.constant.db_fields import OrderFields
from ec_base.common.constant.master import MasterOrderStatusID, MasterShippingStatusID, MasterPaymentStatusID
from ec_base.order.models import Order
from ec_base.order_item.models import OrderItem
from ec_customer.order_item.services.order_item import OrderItemSvc


class OrderSvc:
    @staticmethod
    def create(data, serializer):
        with transaction.atomic():
            order_items = data.pop(OrderFields.ORDER_ITEMS)
            data[OrderFields.STATUS_ID] = MasterOrderStatusID.ORDERED
            data[OrderFields.SHIPPING_STATUS_ID] = MasterShippingStatusID.UNDELIVERED
            data[OrderFields.PAYMENT_STATUS_ID] = MasterPaymentStatusID.UNPAID
            order = Order.objects.create(**data)
            order_item_svc = OrderItemSvc()
            order_item_svc.bulk_create(order_id=order.id, order_items=order_items)
            return serializer(instance=order)

    @staticmethod
    def cancel(order):
        with transaction.atomic():
            order.status_id = MasterOrderStatusID.CANCELED
            order.save()
            order_items = OrderItem.objects.filter(order_id=order.id)
            order_item_svc = OrderItemSvc()
            order_item_svc.bulk_cancel(order_items=order_items)
            return order
