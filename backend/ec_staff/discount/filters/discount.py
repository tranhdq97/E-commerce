from ec_base.common.constant.db_fields import CommonFields, DiscountFields, MasterFields


class DiscountListQueryFields:
    SEARCH_FIELDS = ("__".join([DiscountFields.DISCOUNT_TYPE, MasterFields.NAME]),
                     "__".join([DiscountFields.DISCOUNT_RATE, MasterFields.NAME]))
    ORDER_FIELDS = ("__".join([DiscountFields.DISCOUNT_TYPE, MasterFields.NAME]), CommonFields.ID,)
    ORDER_DEFAULT_FIELD = CommonFields.ID
