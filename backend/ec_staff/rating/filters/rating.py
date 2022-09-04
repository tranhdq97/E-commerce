from ec_base.common.constant.db_fields import CommonFields, RatingFields


class RatingListQueryFields:
    SEARCH_FIELDS = ()
    ORDER_FIELDS = (CommonFields.ID,)
    ORDER_DEFAULT_FIELD = f'{CommonFields.ID}'
    FILTERSET_FIELDS = (RatingFields.PRODUCT_ID,)
