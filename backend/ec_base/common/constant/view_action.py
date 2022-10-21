from ec_base.common.utils.utils import BaseEnum


class BaseViewAction(str, BaseEnum):
    LIST = "list"
    RETRIEVE = "retrieve"
    CREATE = "create"
    UPDATE = "update"
    DESTROY = "destroy"


class OrderViewAction(str, BaseEnum):
    CANCEL = "cancel"


class ProductViewAction(str, BaseEnum):
    UPDATE_QUANTITY = "update_quantity"


class ProductCategoryViewAction(str, BaseEnum):
    GET_SALE_QUANTITY_OVERVIEW = "get_sale_quantity_overview"
    GET_SALE_AMOUNT_OVERVIEW = "get_sale_amount_overview"
