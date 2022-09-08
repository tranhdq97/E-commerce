from ec_base.common.constant import message
from ec_base.common.constant.db_fields import OrderItemFields
from ec_base.common.utils.exceptions import APIErr
from ec_base.order_item.models import OrderItem


class OrderItemSvc:
    @staticmethod
    def validate_quantity(product, quantity):
        if quantity == 0:
            raise APIErr(message.QUANTITY_IS_ZERO % {'name': product.name})

        if quantity > product.quantity:
            raise APIErr(message.NOT_ENOUGH_QUANTITY % {'name': product.name, 'quantity': product.quantity})

        return product

    def bulk_create(self, order_id, order_items):
        for item in order_items:
            discounts = item.pop(OrderItemFields.DISCOUNTS)
            quantity = item.get(OrderItemFields.QUANTITY)
            order_item = OrderItem.objects.create(order_id=order_id, **item)
            order_item.discounts.set(discounts)
            product = self.validate_quantity(order_item.product, quantity)
            product.quantity -= quantity
            product.save()

    def bulk_cancel(self, order_items):
        for item in order_items:
            product = item.product
            product.quantity += item.quantity
            product.save()
