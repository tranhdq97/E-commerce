from ec_base.common.constant.db_fields import CommonFields, UserFields, UserInfoFields


class CustomerListQueryFields:
    SEARCH_FIELDS = (
        "__".join([UserFields.INFO, UserInfoFields.PHONE_NUMBER]),
        "__".join([UserFields.INFO, UserInfoFields.FIRST_NAME]),
    )
    ORDER_FIELDS = (CommonFields.ID,)
    ORDER_DEFAULT_FIELD = f"{CommonFields.ID}"
