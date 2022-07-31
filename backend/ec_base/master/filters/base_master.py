from ...common.constant.db_fields import MasterFields, CommonFields


class BaseMasterListQueryFields:
    SEARCH_FIELDS = (MasterFields.NAME,)
    ORDER_FIELDS = (MasterFields.NAME, CommonFields.ID,)
    ORDER_DEFAULT_FIELD = f'{MasterFields.NAME}'
