from ec_base.common.constant.db_fields import OrderFields
from ec_base.master.serializers.base_master import BaseMasterRetrieveSlz
from ec_base.order.serializers.order import OrderBaseSlz
from ec_customer.order_item.serializers.order_item import OrderItemCreateSlz, OrderItemRetrieveSlz


class OrderCreateSlz(OrderBaseSlz):
    order_items = OrderItemCreateSlz(many=True, required=False)

    class Meta:
        model = OrderBaseSlz.Meta.model
        fields = OrderBaseSlz.Meta.fields + (OrderFields.ORDER_ITEMS,)


class OrderRetrieveSlz(OrderBaseSlz):
    order_items = OrderItemRetrieveSlz(many=True)
    status = BaseMasterRetrieveSlz(many=False)
    shipping_status = BaseMasterRetrieveSlz(many=False)
    payment_status = BaseMasterRetrieveSlz(many=False)

    class Meta:
        model = OrderBaseSlz.Meta.model
        fields = OrderBaseSlz.Meta.fields + (
            OrderFields.STATUS,
            OrderFields.SHIPPING_STATUS,
            OrderFields.PAYMENT_STATUS,
            OrderFields.ORDER_ITEMS,
        )


class OrderListSlz(OrderBaseSlz):
    class Meta:
        model = OrderBaseSlz.Meta.model
        fields = OrderBaseSlz.Meta.fields
