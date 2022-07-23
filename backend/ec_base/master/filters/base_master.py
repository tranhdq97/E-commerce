from ...common.constant.db_fields import MasterFields


class BaseMasterListQueryFields:
    SEARCH_FIELDS = (MasterFields.NAME,)
    ORDER_FIELDS = (MasterFields.NAME, MasterFields.ID,)
    ORDER_DEFAULT_FIELD = f'{MasterFields.NAME}'
