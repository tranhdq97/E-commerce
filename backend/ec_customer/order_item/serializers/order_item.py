from rest_framework import serializers

from ec_base.common.constant.db_fields import OrderItemFields
from ec_base.common.utils.serializer import ForeignKeyField
from ec_base.discount.models import Discount
from ec_base.order_item.serializers.order_item import OrderItemBaseSlz
from ec_base.product.models import Product
from ec_customer.discount.serializers.discount import DiscountForOrderItemRetrieveSlz
from ec_customer.product.serializers.product import ProductForOrderItemRetrieveSlz


class OrderItemCreateSlz(OrderItemBaseSlz):
    product_id = ForeignKeyField(model=Product, required=True)
    discounts = serializers.PrimaryKeyRelatedField(many=True, queryset=Discount.objects.all())

    class Meta:
        model = OrderItemBaseSlz.Meta.model
        fields = OrderItemBaseSlz.Meta.fields + (
            OrderItemFields.PRODUCT_ID, OrderItemFields.QUANTITY, OrderItemFields.DISCOUNTS,
        )


class OrderItemRetrieveSlz(OrderItemBaseSlz):
    product = ProductForOrderItemRetrieveSlz(many=False)
    discounts = DiscountForOrderItemRetrieveSlz(many=True)

    class Meta:
        model = OrderItemBaseSlz.Meta.model
        fields = OrderItemBaseSlz.Meta.fields + (
            OrderItemFields.PRODUCT, OrderItemFields.DISCOUNTS, OrderItemFields.QUANTITY
        )
