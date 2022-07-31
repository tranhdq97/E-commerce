from ...common.constant.db_fields import CommonFields, CustomerFields, UserInfoFields


class CustomerListQueryFields:
    SEARCH_FIELDS = ('__'.join([CustomerFields.INFO, UserInfoFields.PHONE_NUMBER]),
                     '__'.join([CustomerFields.INFO, UserInfoFields.FIRST_NAME]),)
    ORDER_FIELDS = (CommonFields.ID,)
    ORDER_DEFAULT_FIELD = f'{CommonFields.ID}'
