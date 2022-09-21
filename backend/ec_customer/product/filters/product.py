from ec_base.common.constant.db_fields import CommonFields, ProductFields, MasterFields


class ProductListQueryFields:
    SEARCH_FIELDS = (
        ProductFields.NAME,
        "__".join(
            (ProductFields.CATEGORY, MasterFields.NAME),
        ),
    )
    ORDER_FIELDS = (
        CommonFields.ID,
        ProductFields.PRICE,
        ProductFields.QUANTITY,
    )
    ORDER_DEFAULT_FIELD = f"{CommonFields.ID}"
    FILTERSET_FIELDS = (ProductFields.CATEGORY_ID,)
