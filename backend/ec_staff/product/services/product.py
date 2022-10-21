from ec_base.common.constant import message
from ec_base.common.utils.exceptions import APIErr


class ProductSvc:
    @staticmethod
    def update_quantity(product, new_quantity):
        updated_quantity = product.quantity + new_quantity
        if updated_quantity < 0:
            raise APIErr(detail=message.INVALID_INPUT)

        product.quantity = updated_quantity
        product.save()
        return product
